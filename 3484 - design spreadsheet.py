class Spreadsheet(object):

    def __init__(self, rows):
        """
        :type rows: int
        """
        self.sheet = {x : [0] * (rows+1) for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
        

    def setCell(self, cell, value):
        """
        :type cell: str
        :type value: int
        :rtype: None
        """
        col = cell[0]
        row = int(cell[1:])

        self.sheet[col][row] = value
        

    def resetCell(self, cell):
        """
        :type cell: str
        :rtype: None
        """
        self.setCell(cell, 0)

    def getValue(self, formula):
        """
        :type formula: str
        :rtype: int
        """
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        l, r = formula[1:].split('+')

        if l[0] in alpha:
            l = self.sheet[l[0]][int(l[1:])]
        else:
            l = int(l)
        
        if r[0] in alpha:
            r = self.sheet[r[0]][int(r[1:])]
        else:
            r = int(r)
        
        return l + r


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)