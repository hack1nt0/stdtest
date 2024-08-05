from PySide6.QtGui import QKeyEvent, QMouseEvent, QResizeEvent
from stdtest import *
import math


class Mode(enum.Enum):
    DRAW = "Draw"
    DRAG = "Drag"
    ERASE = "Erase"
    ZOOM = "Zoom"


class GView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)

        # self.setBackgroundBrush(BLUE)

        scene = QGraphicsScene(self)
        # scene.setSceneRect(QRectF(QPointF(0, 0), self.size().toSizeF()))
        # scene.setItemIndexMethod(QGraphicsScene.NoIndex)
        # scene.setBackgroundBrush(self.backgroundBrush())
        # scene.setForegroundBrush(self.foregroundBrush())
        # # scene.setSceneRect(-200, -200, 400, 400)
        self.setScene(scene)
        self.setSceneRect(QRectF(QPointF(0, 0), self.size().toSizeF()))
        # self.setCacheMode(QGraphicsView.CacheBackground)
        # self.setRenderHint(QPainter.Antialiasing)
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorViewCenter)

        # self.scale(0.8, 0.8)
        # self.setMinimumSize(400, 400)
        self.mode = None
        self.line_start = None
        self.drag_start = None

        self.pen = QPen(Qt.GlobalColor.blue, 1)
        self.brush = QBrush(Qt.GlobalColor.blue)
    

    def resizeEvent(self, event: QResizeEvent) -> None:
        # if self.scene():
        #     self.scene().setSceneRect(QRectF(QPointF(0, 0), event.size().toSizeF()))
        self.setSceneRect(QRectF(QPointF(0, 0), self.size().toSizeF()))
        return super().resizeEvent(event)

    def set_color(self, color: QColor):
        self.pen = QPen(color, 1)
        self.brush = QBrush(color)
    
    def keyPressEvent(self, event: QKeyEvent) -> None:
        # print(event, flush=T)
        match event.key(): 
            case Qt.Key.Key_Control:
                self.mode = Mode.DRAW
            case Qt.Key.Key_Shift:
                self.mode = Mode.ERASE
        return super().keyPressEvent(event)
    
    def keyReleaseEvent(self, event: QKeyEvent) -> None:
        # print(event, flush=T)
        match event.key():
            case Qt.Key.Key_Control:
                self.mode = None
                self.line_start = None
            case Qt.Key.Key_Shift:
                self.mode = None
        return super().keyReleaseEvent(event)

    def clear(self):
        self.scene().clear()

    def setItem(self, item):
        self.scene().clear()
        self.scene().addItem(item)

    def addItem(self, item):
        self.scene().addItem(item)

    def delItem(self, item):
        self.scene().removeItem(item)

    def wheelEvent(self, event: QWheelEvent) -> None:
        # print(event.scenePosition())
        
        delta = event.angleDelta().y()
        self.scale_view(math.pow(2.0, -delta / 240.0))
        # return super().wheelEvent(event)

    def scale_view(self, scaleFactor):
        scaleAcc = (
            self.transform().scale(scaleFactor, scaleFactor).mapRect(QRectF(0, 0, 1, 1))
        )
        if scaleAcc.width() < 0.1 or scaleAcc.width() > 100:
            return
        self.scale(scaleFactor, scaleFactor)
        # for scrollbar in [self.horizontalScrollBar(), self.verticalScrollBar()]:
        #     print(f"{scrollbar.minimum()} <= {scrollbar.value()} <= {scrollbar.maximum()}")

    def draw_circle(self, pos: QPoint):
        pos = self.mapToScene(pos)
        x, y = pos.x(), pos.y()
        w, h = 10, 10
        self.scene().addEllipse(x, y, w, h, self.pen, self.brush)

    def draw_line(self, start: QPoint, end: QPoint):
        start = self.mapToScene(start)
        end = self.mapToScene(end)
        self.scene().addLine(QLineF(start, end), self.pen)

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        pos = event.pos()
        item_under_cursor: QGraphicsEllipseItem = self.itemAt(pos)
        # item_under_cursor.setPen(YELLOW)
        # item_under_cursor.setBrush(YELLOW)
        item_under_cursor.setSelected(T)
        # TODO highlight clicked item(s)
        return super().mouseDoubleClickEvent(event)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.mode = Mode.DRAG
        self.drag_start = event.pos()
        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        match self.mode:
            case Mode.DRAG:
                dir = self.drag_start - event.pos()
                self.setTransform(self.transform().translate(dir.x(), dir.y()))
            case Mode.DRAW:
                self.draw_circle(event.pos())
                # if not self.line_start:
                #     self.line_start = event.pos()
                # line_end = event.pos()
                # self.draw_line(self.line_start, line_end)
                # self.line_start = line_end
            case Mode.ERASE:
                pos = event.pos()
                item_under_cursor = self.itemAt(pos)
                print(pos, item_under_cursor, flush=T)
                if item_under_cursor is not None:
                    item_under_cursor.prepareGeometryChange() #TODO
                    self.scene().removeItem(item_under_cursor)
                    del item_under_cursor
                print(len(self.items()), flush=T)
        return super().mouseMoveEvent(event)
    

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.mode = None
        self.drag_start = None
        return super().mouseReleaseEvent(event)

    def save_png(self):
        image = QImage(
            self.scene().itemsBoundingRect().size().toSize(), QImage.Format.Format_ARGB32
        )
        self.scene()
        painter = QPainter(image)
        self.scene().render(painter)
        painter.end()
        self.png_fn, _ = QFileDialog.getSaveFileName(
            self,
            caption="Saved As png",
            dir=os.getcwd(),
            filter="*.png",
            selectedFilter="*.png",
        )
        image.save(self.png_fn)

    def save_svg(self):
        from PySide6.QtSvg import QSvgGenerator
        image = QSvgGenerator()
        self.file, _ = QFileDialog.getSaveFileName(
            self,
            caption="Saved As Svg",
            dir=os.getcwd(),
            filter="*.svg",
            selectedFilter="*.svg",
        )
        image.setFileName(self.file)
        bbox = self.scene().itemsBoundingRect()
        image.setSize(bbox.size().toSize())
        image.setViewBox(QRectF(0., 0., bbox.width(), bbox.height()))
        image.setTitle("")
        image.setDescription("")
        painter = QPainter(image)
        self.scene().clearSelection() #TODO
        self.scene().render(painter)
        painter.end()