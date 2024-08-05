from stdtest import *
import math


class GViewer(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)

        # self.setBackgroundBrush(BLUE)

        scene = QGraphicsScene(self)
        scene.setItemIndexMethod(QGraphicsScene.NoIndex)
        scene.setBackgroundBrush(self.backgroundBrush())
        scene.setForegroundBrush(self.foregroundBrush())
        # scene.setSceneRect(-200, -200, 400, 400)
        self.setScene(scene)
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setRenderHint(QPainter.Antialiasing)
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorViewCenter)

        # self.scale(0.8, 0.8)
        # self.setMinimumSize(400, 400)
        self.start_drag = False

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

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.start_drag = event.pos()
        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.start_drag:
            dir = self.start_drag - event.pos()
            self.setTransform(self.transform().translate(dir.x(), dir.y()))
        return super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.start_drag = None
        return super().mouseReleaseEvent(event)

#### ====================================
    def set_dot(self, dot: str):
        import tempfile
        from PySide6.QtSvgWidgets import QSvgWidget, QGraphicsSvgItem

        with (
            tempfile.NamedTemporaryFile("w", suffix=".svg", delete=F) as svgfile,
            tempfile.NamedTemporaryFile("w+") as dotfile,
        ):
            dotfile.write(dot)
            dotfile.flush()
            cmd = f"{'wsl ' if entity._WIN else ''}dot -Tsvg -Kdot -o {svgfile.name} {dotfile.name}"
            subprocess.run(
                cmd,
                shell=T,
                stderr=PIPE,
                check=T,
            )
            self.svgitem = QGraphicsSvgItem(svgfile.name)
            self.setItem(self.svgitem)
            self.setSceneRect(self.svgitem.boundingRect())
            # self.setMinimumSize(self.svgitem.boundingRect().size().toSize())

            
            return svgfile.name
    
