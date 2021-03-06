import sys
import math
import json
import transformation


class StopPointGrid:
    def __init__( self, nm, layer, direction, width, pitch, offset=0):
        self.nm = nm
        self.layer = layer
        self.direction = direction
        assert direction in ['v','h']
        self.width = width
        self.pitch = pitch
        self.offset = offset
        assert pitch > width > 0

        self.grid = []
        self.legalStopVector = []
        self.legalStopIndices = set()

    def addGridPoint( self, value, isLegal):
        self.grid.append( value)
        self.legalStopVector.append( isLegal)
        if isLegal:
            self.legalStopIndices.add( len(self.grid)-1)

    @property
    def n( self):
        return len(self.grid)-1

    def value( self, idx):
        whole = idx // self.n
        fract = idx % self.n
        while fract < 0:
            whole -= 1
            fract += self.n
        assert fract in self.legalStopIndices
        return whole * self.grid[-1] + self.grid[fract]

    def segment( self, netName, center, bIdx, eIdx):
        c = center*self.pitch + self.offset
        c0 = c - self.width//2
        c1 = c + self.width//2
        if self.direction == 'h':
             rect = [ bIdx, c0, eIdx, c1]
        else:
             rect = [ c0, bIdx, c1, eIdx]
        return { 'netName' : netName, 'layer' : self.layer, 'rect' : rect}

class UnitCell:

    def computeBbox( self):
        self.bbox = transformation.Rect(None,None,None,None)
        for term in self.terminals:
            r = transformation.Rect( *term['rect'])
            if self.bbox.llx is None or self.bbox.llx > r.llx: self.bbox.llx = r.llx
            if self.bbox.lly is None or self.bbox.lly > r.lly: self.bbox.lly = r.lly
            if self.bbox.urx is None or self.bbox.urx < r.urx: self.bbox.urx = r.urx
            if self.bbox.ury is None or self.bbox.ury < r.ury: self.bbox.ury = r.ury

    def __init__( self):
        self.terminals = []
        m0Pitch  = 36
        m1Pitch  = 36
        m2Pitch  = 36
        m3Pitch  = 36 
        plPitch  = 36
        plOffset = 0
        v1Pitch  = 36
        v2Pitch  = 36
        dcPitch  = 36

        assert dcPitch == plPitch
        
        m0Width = 18
        m1Width = 18
        m2Width = 18
        m3Width = 18
        dcWidth = 18
        plWidth = 18
        v1Width = 18
        v2Width = 18

        stoppoint = (dcWidth//2 + plOffset-plWidth//2)//2
        self.m0 = StopPointGrid( 'm0', 'M0', 'h', width=m0Width, pitch=m0Pitch)
        self.m0.addGridPoint( 0,                 False)
        self.m0.addGridPoint( stoppoint,         True)
        self.m0.addGridPoint( plOffset,          False)
        self.m0.addGridPoint( dcPitch-stoppoint, True)
        self.m0.addGridPoint( dcPitch,           False)

        self.m1 = StopPointGrid( 'm1', 'M1', 'v', width=m1Width, pitch=m1Pitch, offset=m1Width/2)
        self.m1.addGridPoint( 0,                   False)
        self.m1.addGridPoint( stoppoint,           True)
        self.m1.addGridPoint( 2*m0Pitch,           False)
        self.m1.addGridPoint( 4*m0Pitch-stoppoint, True)
        self.m1.addGridPoint( 4*m0Pitch,           False)

        
        self.m2 = StopPointGrid( 'm2', 'M2', 'h', width=m2Width, pitch=m2Pitch, offset=m2Width/2)
        self.m2.addGridPoint( 0,                 False)
        self.m2.addGridPoint( stoppoint,         True)
        self.m2.addGridPoint( 2*m0Pitch,          False)
        self.m2.addGridPoint( 4*m0Pitch-stoppoint, True)
        self.m2.addGridPoint( 4*m0Pitch,           False)

        self.m3 = StopPointGrid( 'm3', 'M3', 'v', width=m3Width, pitch=m3Pitch, offset=m3Width/2)
        self.m3.addGridPoint( 0,                   False)
        self.m3.addGridPoint( stoppoint,           True)
        self.m3.addGridPoint( 2*m0Pitch,           False)
        self.m3.addGridPoint( 4*m0Pitch-stoppoint, True)
        self.m3.addGridPoint( 4*m0Pitch,           False)

        self.pl = StopPointGrid( 'pl', 'poly', 'v', width=plWidth, pitch=plPitch, offset=plOffset)
        self.pl.addGridPoint( 0,                   False)
        self.pl.addGridPoint( stoppoint,           True)
        self.pl.addGridPoint( 2*m0Pitch,           False)
        self.pl.addGridPoint( 4*m0Pitch-stoppoint, True)
        self.pl.addGridPoint( 4*m0Pitch,           False)

        self.dc = StopPointGrid( 'dc', 'diffcon', 'v', width=dcWidth, pitch=dcPitch)
        self.dc.addGridPoint( 0,                   False)
        self.dc.addGridPoint( stoppoint,           True)
        self.dc.addGridPoint( 2*m0Pitch,           False)
        self.dc.addGridPoint( 4*m0Pitch-stoppoint, True)
        self.dc.addGridPoint( 4*m0Pitch,           False)

        self.v1 = StopPointGrid( 'v1', 'via1', 'v', width=v1Width, pitch=v1Pitch, offset=v1Width/2)
        self.v1.addGridPoint( 0,                   False)
        self.v1.addGridPoint( stoppoint,           True)
        self.v1.addGridPoint( 2*m0Pitch,           False)
        self.v1.addGridPoint( 4*m0Pitch-stoppoint, True)
        self.v1.addGridPoint( 4*m0Pitch,           False)

        self.v2 = StopPointGrid( 'v2', 'via2', 'v', width=v2Width, pitch=v2Pitch, offset=v1Width/2)
        self.v2.addGridPoint( 0,                   False)
        self.v2.addGridPoint( stoppoint,           True)
        self.v2.addGridPoint( 2*m0Pitch,           False)
        self.v2.addGridPoint( 4*m0Pitch-stoppoint, True)
        self.v2.addGridPoint( 4*m0Pitch,           False)

    def addSegment( self, grid, netName, c, bIdx, eIdx):
        segment = grid.segment( netName, c, bIdx, eIdx)
        self.terminals.append( segment)
        return segment
        
    def m0Segment( self, netName, x0, x1, y): return self.addSegment( self.m0, netName, y, x0, x1)
    def m1Segment( self, netName, x, y0, y1): return self.addSegment( self.m1, netName, x, y0, y1)
    def m2Segment( self, netName, x0, x1, y): return self.addSegment( self.m2, netName, y, x0, x1)
    def m3Segment( self, netName, x, y0, y1): return self.addSegment( self.m3, netName, x, y0, y1)
    def plSegment( self, netName, x, y0, y1): return self.addSegment( self.pl, netName, x, y0, y1)
    def dcSegment( self, netName, x, y0, y1): return self.addSegment( self.dc, netName, x, y0, y1)
    def v1Segment( self, netName, x, y0, y1): return self.addSegment( self.v1, netName, x, y0, y1)
    def v2Segment( self, netName, x, y0, y1): return self.addSegment( self.v2, netName, x, y0, y1)

    def unit( self, x, y):
        Pitch = 36
        width = 18
        v1_width = 18
        v1_enclosure = 5
        x_number = int(2 *round(((x_length + Pitch - width)/(2.0*Pitch))))
        y_number = int(2 *round(((y_length + Pitch - width)/(2.0*Pitch))))
        x_length1 = (x_number - 1) * Pitch + width
        y_length1 = (y_number - 1) * Pitch + width
        for i in range(x_number):
            uc.m1Segment( 'm1', (i+(x*x_number)+x), ((y*y_length1)+(y*54) - v1_enclosure), ((1+y)*y_length1)+(y*54) + v1_enclosure)
            uc.m3Segment( 'm3', (i+(x*x_number)+x), ((y*y_length1)+(y*54) - v1_enclosure), ((1+y)*y_length1)+(y*54) + v1_enclosure)
            if (i % 2) == 0:
                uc.v1Segment( 'v1', (i+(x*x_number)+x), (((1+y)*y_length1)+(y*54)-v1_width), ((1+y)*y_length1)+(y*54))
                uc.v2Segment( 'v2', (i+(x*x_number)+x), (((1+y)*y_length1)+(y*54)-v1_width), ((1+y)*y_length1)+(y*54))
            else:
                uc.v1Segment( 'v1', (i+(x*x_number)+x), ((y*y_length1)+(y*54)), (((y*y_length1)+(y*54)) + v1_width))
                uc.v2Segment( 'v2', (i+(x*x_number)+x), ((y*y_length1)+(y*54)), (((y*y_length1)+(y*54)) + v1_width))
        for i in range(y_number):
            uc.m2Segment( 'm2', (0+(x*x_length1)+(x*54) - v1_enclosure), (x_length1*(1+x)+(x*54) + v1_enclosure), (i+(y*y_number)+y))
            if (i % 2) == 0:
                uc.v1Segment( 'v1', (x_number + (x*x_number) + x- 1), (((y*y_length1)+(y*54)) + (2*i*width)), (((y*y_length1)+(y*54)) + ((2*i + 1)*width)))
                uc.v2Segment( 'v2', (x_number + (x*x_number) + x - 1), (((y*y_length1)+(y*54)) + (2*i*width)), (((y*y_length1)+(y*54)) + ((2*i + 1)*width)))
            else:
                uc.v1Segment( 'v1', (x*x_number) + x, (((y*y_length1)+(y*54)) + (2*i*width)), (((y*y_length1)+(y*54)) + ((2*i + 1)*width)))
                uc.v2Segment( 'v2', (x*x_number) + x, (((y*y_length1)+(y*54)) + (2*i*width)), (((y*y_length1)+(y*54)) + ((2*i + 1)*width)))

if __name__ == "__main__":
    unit_cap = int(sys.argv[1])
    x_cells = int(sys.argv[2])
    y_cells = int(sys.argv[3])
    x_length = float((math.sqrt(unit_cap/2))*1000)
    y_length = float((math.sqrt(unit_cap/2))*1000)  
    uc = UnitCell()
    for (x,y) in ( (x,y) for x in range(x_cells) for y in range(y_cells)):
        uc.unit( x, y)
    uc.computeBbox()

    with open( "./mydesign_dr_globalrouting.json", "wt") as fp:
        data = { 'bbox' : uc.bbox.toList(), 'globalRoutes' : [], 'globalRouteGrid' : [], 'terminals' : uc.terminals}
        fp.write( json.dumps( data, indent=2) + '\n')

