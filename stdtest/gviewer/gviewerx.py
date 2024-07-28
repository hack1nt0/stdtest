from stdtest import *
from .gwidget_ui import Ui_GWidget
from PySide6.QtSvgWidgets import QSvgWidget, QGraphicsSvgItem
import tempfile


@dataclasses.dataclass
class GItem:
    props: Dict[str, Any]
    items: List[QGraphicsItem]


PAD = 4  # https://stackoverflow.com/questions/76349251/converting-between-pixels-and-graphviz-sizes-coordinates
LABEL_ITEM_BRUSH = QBrush(QColor(255, 255, 0))
LABEL_ITEM_PEN = QPen(BLACK)
# ITEM_BRUSH = QBrush(BLUE, Qt.BrushStyle.DiagCrossPattern)
ITEM_BRUSH = QBrush(QColor(0, 0, 255))
ITEM_PEN = Qt.PenStyle.NoPen


def parse_node(dats: List[Dict], H: int) -> QAbstractGraphicsShapeItem:
    ret = None
    for dat in dats:
        match dat["op"]:
            case "e":
                x, y, w, h = dat["rect"]
                x = x - w + PAD
                y = H - (y + h) + PAD
                w *= 2
                h *= 2
                ret = QGraphicsEllipseItem(x, y, w, h)
            case "b":
                pass
    if ret:
        ret.setBrush(ITEM_BRUSH)
        ret.setPen(ITEM_PEN)
    return ret


def parse_edge(dats: List[Dict], H: int) -> QAbstractGraphicsShapeItem:
    pass


import math


def parse_text(dats: List[Dict[str, Any]], H: int) -> List[QAbstractGraphicsShapeItem]:
    rets = []
    texts = []
    fontH = math.inf
    minX = math.inf
    maxW = 0
    minY, maxY = math.inf, 0
    lines = 0
    for dat in dats:
        match dat["op"]:
            case "F":
                fontH = dat["size"]
            case "T":
                texts.append(dat["text"])
                x, y = dat["pt"]
                width = dat["width"]
                # match dat['align']:
                #     case 'l':
                #         pass
                #     case 'c':
                #         x -= width / 2
                #     case 'r':
                #         x -= width
                minX = min(minX, x)
                minY = min(minY, y)
                maxY = max(maxY, y + fontH)
                lines += 1
                maxW = max(maxW, width)
    # size = size * 4 / 3
    x = minX + PAD
    # y = H - (y + size / 2) + PAD #TODO
    y = H - maxY + PAD
    w = maxW + PAD
    h = maxY - minY + PAD

    ret_text = QGraphicsTextItem("\n".join(texts))
    ret_text.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
    ret_text.moveBy(x, y)

    QGraphicsPolygonItem
    QPolygonF

    w = ret_text.boundingRect().width()
    h = ret_text.boundingRect().height()
    ret_bb = QGraphicsRectItem(x, y, w, h)
    ret_bb.setBrush(LABEL_ITEM_BRUSH)
    ret_bb.setPen(LABEL_ITEM_PEN)

    rets.append(ret_bb)
    rets.append(ret_text)
    return rets


def parse_props(dat: Dict[str, Any]):
    ret = {}
    PREFIX = "cchelper_"
    for k, v in dat.items():
        if k.startswith(PREFIX):
            k = k[len(PREFIX) :]
            ret[k] = v
    return ret


def parse_gitems(dat: Dict) -> List[GItem]:
    _, _, _, H = map(float, dat["bb"].split(","))
    # H += PAD * 2
    rets = []
    nodes, edges = 0, 0
    for o in dat.get("objects", []):
        if "_draw_" not in o:
            continue
        ret = GItem({}, [])
        ret.props["name"] = o["name"]
        ret.props.update(parse_props(o))
        ret.items.append(parse_node(o["_draw_"], H))
        if "_ldraw_" in o:
            ret.items.extend(parse_text(o["_ldraw_"], H))
        rets.append(ret)
        nodes += 1
    for o in dat.get("edges", []):
        if "_draw_" not in o:
            continue
        ret = GItem({}, [])
        ret.props.update(parse_props(o))
        # ret.items.append(parse_node(o["_draw_"], H))
        if "_ldraw_" in o:
            ret.items.extend(parse_text(o["_ldraw_"], H))
        rets.append(ret)
        edges += 1
    return nodes, edges, rets


class GViewerX(QWidget, Ui_GWidget):

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.generateButton.clicked.connect(self.refresh)
        
        self.layoutsmenu = QMenu(self)
        # self.LMenu = QMenu(self)
        self.layoutsgroup = QActionGroup(self)
        for L in [
            "dot",
            "neato",
            "fdp",
            "sfdp",
            "circo",
            "twopi",
        ]:
            act: QAction = self.layoutsgroup.addAction(
                self.layoutsmenu.addAction(L, self.refresh)
            )
            act.setCheckable(T)
            if L == "dot":
                act.setChecked(T)
        self.layoutButton.setMenu(self.layoutsmenu)

        self.lineEdit.returnPressed.connect(self.filter)
        self.clearfindButton.clicked.connect(self.clear_found)

        self.gitems: List[GItem] = []

        self.DEFAULT_COLOR = f"""
    bgcolor="#000080";
	node [color=white fontcolor=white];
	edge [color=white];
"""

        self.c_menu = QMenu(self)
        self.fitscreenButton.clicked.connect(self.fit_scene_to_view)
        self.actualsizeButton.clicked.connect(self.reset_scale)
        self.savepngButton.clicked.connect(self.save_png)
        self.copysvgButton.clicked.connect(self.copy_svg)

        # self.refresh()
        self.svgitem: QGraphicsSvgItem = None
        self.svgfile: str = None

    @property
    def layout_(self):
        return [
            action.text() for action in self.layoutsmenu.actions() if action.isChecked()
        ][0]

    @property
    def source(self) -> str:
        return self.textEdit.toPlainText()

    def refresh(self):
        self.svgfile = self.view.set_dot(self.source)
        # self.nodes, self.edges, self.gitems = parse_gitems(dat)
        # self.label.setText(f"{self.nodes}/{self.edges}")

    def copy_svg(self):
        if not self.svgfile:
            return
        QGuiApplication.clipboard().setText(open(self.svgfile).read())

    def reset_found(self):
        for e in self.view.items():
            if e != self.svgitem:
                self.view.delItem(e)
    
    def clear_found(self):
        self.reset_found()
        self.lineEdit.clear()

    def filter(self):
        self.reset_found()
        Q = self.lineEdit.text()
        M = 0
        for gitem in self.gitems:
            ok = False
            try:
                ok = eval(Q, gitem.props)
            except BaseException as e:
                # logger.exception(e)
                pass
            if ok:
                M += 1
                for item in gitem.items:
                    self.view.addItem(item)
        logger.info(f"Found {M} items")

    def fit_scene_to_view(self):
        sw, wh = self.view.sceneRect().width(), self.view.sceneRect().height()
        vw, vh = self.view.width(), self.view.height()
        scaleFactor = min(vw / sw, vh / wh)
        self.view.resetTransform()
        self.view.scale(scaleFactor, scaleFactor)

    def reset_scale(self):
        self.view.resetTransform()
        # self.view.setTransform(QTransform(1, 0, 0, 1, 0, 0), combine=False)

    def save_png(self):
        if self.svgitem is None:
            logger.error("Please edit/Save dot file first!")
            return
        image = QImage(
            self.svgitem.boundingRect().size().toSize(), QImage.Format.Format_ARGB32
        )
        painter = QPainter(image)
        self.svgitem.renderer().render(painter)
        painter.end()
        self.png_fn, _ = QFileDialog.getSaveFileName(
            self,
            caption="Saved As png",
            dir=os.getcwd(),
            filter="*.png",
            selectedFilter="*.png",
        )
        image.save(self.png_fn)
        logger.info(f"Saved as {self.png_fn}")

