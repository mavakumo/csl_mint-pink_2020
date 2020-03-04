import shapefile as shp  # Requires the pyshp package
import matplotlib.pyplot as plt


class Stadtteil:
    def __init__(self, shape):
        self.Name = shape.record[0]
        self.Area = shape.record[3]
        self.x = [i[0] for i in shape.shape.points[:]]
        self.y = [i[1] for i in shape.shape.points[:]]

    def __str__(self):
        return self.Name

    def __repr__(self):
        return self.Name

    def draw(self,farbe):
        plt.fill(self.x,self.y, farbe)

def init():
    sf = shp.Reader("Stadtteile.shp", encoding="ISO8859-1")
    stadtteile = []

    for shape in sf.shapeRecords():
        stadtteile.append(Stadtteil(shape))
    return stadtteile

def draw(stadtteile):
    plt.figure()
    for stadtteil in stadtteile:
        if stadtteil.Area > 7155840.27429999970:
            stadtteil.draw("green")
        else:
            stadtteil.draw("red")
    plt.show()

if __name__ == "__main__":
    # stadtteil.Name
    # stadtteil.infizierte

    stadtteile = init()
    print(stadtteile)
    draw(stadtteile)