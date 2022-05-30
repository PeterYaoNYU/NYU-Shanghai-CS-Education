from tkinter import Tk, Canvas

def hanoi(num_disks, start, goal, mid):
    """
    Implement the tower of hanoi algorithm.
    If implemented correctly, a window should pop up, and disks will move as desired.
    to move a disk, you can call
    game.move(num_disks, start, goal)

    :param num_disks: number of disks in this function call.
    :param start: Int -- start moving from this pole
    :param goal: Int -- move to this pole
    :param mid: Int -- Intermediate (useless) pole for this move.

    :return: nothing to return
    """
    if num_disks==1:
        game.move(1, start, goal)
        return None
    hanoi(num_disks-1, start, mid, goal)
    game.move(num_disks, start, goal)
    hanoi(num_disks-1, mid, goal, start)
    return None

# The graphical interface
class Tkhanoi:

    # Create our objects
    def __init__(self, n, bitmap = None):
        self.n = n
        self.tk = tk = Tk()
        self.canvas = c = Canvas(tk)
        c.pack()
        width, height = tk.getint(c['width']), tk.getint(c['height'])

        # Add background
        if bitmap:
            self.bitmap = c.create_bitmap(width//2, height//2,
                                          bitmap=bitmap,
                                          foreground='blue')

        # Generate pegs
        pegwidth = 10
        pegheight = height//2
        pegdist = width//3
        x1, y1 = (pegdist-pegwidth)//2, height*1//3
        x2, y2 = x1+pegwidth, y1+pegheight
        self.pegs = []
        p = c.create_rectangle(x1, y1, x2, y2, fill='black')
        self.pegs.append(p)
        x1, x2 = x1+pegdist, x2+pegdist
        p = c.create_rectangle(x1, y1, x2, y2, fill='black')
        self.pegs.append(p)
        x1, x2 = x1+pegdist, x2+pegdist
        p = c.create_rectangle(x1, y1, x2, y2, fill='black')
        self.pegs.append(p)
        self.tk.update()

        # Generate pieces
        pieceheight = pegheight//16
        maxpiecewidth = pegdist*2//3
        minpiecewidth = 2*pegwidth
        self.pegstate = [[], [], []]
        self.pieces = {}
        x1, y1 = (pegdist-maxpiecewidth)//2, y2-pieceheight-2
        x2, y2 = x1+maxpiecewidth, y1+pieceheight
        dx = (maxpiecewidth-minpiecewidth) // (2*max(1, n-1))
        for i in range(n, 0, -1):
            p = c.create_rectangle(x1, y1, x2, y2, fill='red')
            self.pieces[i] = p
            self.pegstate[0].append(i)
            x1, x2 = x1 + dx, x2-dx
            y1, y2 = y1 - pieceheight-2, y2-pieceheight-2
            self.tk.update()
            self.tk.after(25)

    def run(self):
        hanoi(self.n, 0, 2, 1)

    # Reporting callback for the actual hanoi function
    def move(self, i, a, b):
        if self.pegstate[a][-1] != i: raise RuntimeError # Assertion
        del self.pegstate[a][-1]
        p = self.pieces[i]
        c = self.canvas

        # Lift the piece above peg a
        ax1, ay1, ax2, ay2 = c.bbox(self.pegs[a])
        while 1:
            x1, y1, x2, y2 = c.bbox(p)
            if y2 < ay1: break
            c.move(p, 0, -1)
            self.tk.update()

        # Move it towards peg b
        bx1, by1, bx2, by2 = c.bbox(self.pegs[b])
        newcenter = (bx1+bx2)//2
        while 1:
            x1, y1, x2, y2 = c.bbox(p)
            center = (x1+x2)//2
            if center == newcenter: break
            if center > newcenter: c.move(p, -1, 0)
            else: c.move(p, 1, 0)
            self.tk.update()

        # Move it down on top of the previous piece
        pieceheight = y2-y1
        newbottom = by2 - pieceheight*len(self.pegstate[b]) - 2
        while 1:
            x1, y1, x2, y2 = c.bbox(p)
            if y2 >= newbottom: break
            c.move(p, 0, 1)
            self.tk.update()

        # Update peg state
        self.pegstate[b].append(i)


bitmap = None
game = Tkhanoi(6, bitmap)
game.run()