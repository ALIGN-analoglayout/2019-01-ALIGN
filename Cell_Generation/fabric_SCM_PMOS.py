import sys
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

    def segment( self, netName, pinName, center, bIdx, eIdx):
        c = center*self.pitch + self.offset
        c0 = c - self.width/2
        c1 = c + self.width/2
        if self.direction == 'h':
             rect = [ bIdx, c0, eIdx, c1]
        else:
             rect = [ c0, bIdx, c1, eIdx]
        return { 'netName' : netName, 'pin' : pinName, 'layer' : self.layer, 'rect' : rect}

    def segment1( self, netName, pinName, bIdy, eIdy, bIdx, eIdx):
        rect = [bIdx, bIdy, eIdx, eIdy]
        return { 'netName' : netName, 'pin' : pinName, 'layer' : self.layer, 'rect' : rect}

class UnitCell:

    def computeBbox( self):
        self.bbox = transformation.Rect(None,None,None,None)
        for term in self.terminals:
            r = transformation.Rect( *term['rect'])
            if self.bbox.llx is None or self.bbox.llx > r.llx: self.bbox.llx = r.llx
            if self.bbox.lly is None or self.bbox.lly > r.lly: self.bbox.lly = r.lly
            if self.bbox.urx is None or self.bbox.urx < r.urx: self.bbox.urx = r.urx
            if self.bbox.ury is None or self.bbox.ury < r.ury: self.bbox.ury = r.ury

    def __init__( self ):
        self.terminals = []
        m0Pitch  = 54
        m1Pitch  = 54 
        m2Pitch  = 54 
        m3Pitch  = 54 
        plPitch  = 54 
        plOffset = 10 
        m1Offset = 37
        m2Offset = 9  
        m3Offset = 37 
        v0Pitch  = 36 
        v1Pitch  = m2Pitch 
        v2Pitch  = m2Pitch 
        dcPitch  = 36 
        finPitch = 27 
        m0Width = 18
        m1Width = 18
        m2Width = 18
        m3Width = 18
        dcWidth = 18
        plWidth = 20
        lisdWidth = 24
        sdtWidth = 24
        v0Width = 18
        v1Width = 18
        v2Width = 18
        finWidth = 7
        gcutWidth = 18
        pcWidth = 18
        finDummy = 4
        pc_gateExtension = 1 ###Fig. 1 of Ref. [1]
        pcLength = (gate_u-1)*plPitch + plWidth + (2*pc_gateExtension)
        plActive = 25 ###Fig. 1 of Ref. [1]
        extension_y = 0 
        K_space = extension_y // finPitch 
        fin_enclosure = 10 
        activeWidth1 = finPitch*fin_u
        activeWidth = finPitch*fin_u1
        activePitch = activeWidth1 + (2*finDummy + K_space)*finPitch + extension_y
        activeOffset = (activeWidth/2) + finDummy*finPitch - fin_enclosure
        pcPitch  = activePitch
        gcutPitch  = activePitch
        pc_activeDistance = 30 
        pc_gcutDistance = 7    
        pcOffset = activeOffset + pc_activeDistance + pcWidth/2 + activeWidth/2
        gcutOffset = activePitch - gcutWidth/2

        stoppoint = (dcWidth//2 + plOffset-plWidth//2)//2
        self.m0 = StopPointGrid( 'm0', 'M0', 'h', width=m0Width, pitch=m0Pitch)
        self.m0.addGridPoint( 0,                 False)
        self.m0.addGridPoint( stoppoint,         True)
        self.m0.addGridPoint( plOffset,          False)
        self.m0.addGridPoint( dcPitch-stoppoint, True)
        self.m0.addGridPoint( dcPitch,           False)

        self.m1 = StopPointGrid( 'm1', 'M1', 'v', width=m1Width, pitch=m1Pitch, offset=m1Offset)
        self.m1.addGridPoint( 0,                   False)
        self.m1.addGridPoint( stoppoint,           True)
        self.m1.addGridPoint( 2*m0Pitch,           False)
        self.m1.addGridPoint( 4*m0Pitch-stoppoint, True)
        self.m1.addGridPoint( 4*m0Pitch,           False)
        
        self.m2 = StopPointGrid( 'm2', 'M2', 'h', width=m2Width, pitch=m2Pitch, offset=m2Offset)
        self.m2.addGridPoint( 0,                 False)
        self.m2.addGridPoint( stoppoint,         True)
        self.m2.addGridPoint( 2*m0Pitch,          False)
        self.m2.addGridPoint( 4*m0Pitch-stoppoint, True)
        self.m2.addGridPoint( 4*m0Pitch,           False)

        self.m3 = StopPointGrid( 'm3', 'M3', 'v', width=m3Width, pitch=m3Pitch, offset=m3Offset)
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

        self.v0 = StopPointGrid( 'v0', 'via0', 'v', width=v0Width, pitch=v0Pitch)
        self.v0.addGridPoint( 0,                   False)
        self.v0.addGridPoint( stoppoint,           True)
        self.v0.addGridPoint( 2*m0Pitch,           False)
        self.v0.addGridPoint( 4*m0Pitch-stoppoint, True)
        self.v0.addGridPoint( 4*m0Pitch,           False)
        
        self.v1 = StopPointGrid( 'v1', 'via1', 'h', width=v1Width, pitch=v1Pitch, offset=m2Offset)
        self.v1.addGridPoint( 0,                   False)
        self.v1.addGridPoint( stoppoint,           True)
        self.v1.addGridPoint( 2*m0Pitch,           False)
        self.v1.addGridPoint( 4*m0Pitch-stoppoint, True)
        self.v1.addGridPoint( 4*m0Pitch,           False)

        self.v2 = StopPointGrid( 'v2', 'via2', 'h', width=v2Width, pitch=v2Pitch, offset=m2Offset)
        self.v2.addGridPoint( 0,                   False)
        self.v2.addGridPoint( stoppoint,           True)
        self.v2.addGridPoint( 2*m0Pitch,           False)
        self.v2.addGridPoint( 4*m0Pitch-stoppoint, True)
        self.v2.addGridPoint( 4*m0Pitch,           False)
        
        self.fin = StopPointGrid( 'fin', 'fin', 'h', width=finWidth, pitch=finPitch, offset=finWidth/2)
        self.fin.addGridPoint( 0,                 False)
        self.fin.addGridPoint( stoppoint,         True)
        self.fin.addGridPoint( plOffset,          False)
        self.fin.addGridPoint( dcPitch-stoppoint, True)
        self.fin.addGridPoint( dcPitch,           False)

        self.active = StopPointGrid( 'active', 'active', 'h', width=activeWidth, pitch=activePitch, offset=activeOffset)
        self.active.addGridPoint( 0,                 False)
        self.active.addGridPoint( stoppoint,         True)
        self.active.addGridPoint( plOffset,          False)
        self.active.addGridPoint( dcPitch-stoppoint, True)
        self.active.addGridPoint( dcPitch,           False)

        self.pselect = StopPointGrid( 'pselect', 'pselect', 'v', width=activeWidth, pitch=activePitch, offset=activeOffset)

        self.nwell = StopPointGrid( 'nwell', 'nwell', 'v', width=activeWidth, pitch=activePitch, offset=activeOffset)


        self.gcut = StopPointGrid( 'GCUT', 'GCUT', 'h', width=gcutWidth, pitch=gcutPitch, offset=gcutOffset)
        self.gcut.addGridPoint( 0,                 False)
        self.gcut.addGridPoint( stoppoint,         True)
        self.gcut.addGridPoint( plOffset,          False)
        self.gcut.addGridPoint( dcPitch-stoppoint, True)
        self.gcut.addGridPoint( dcPitch,           False)

        self.gcut1 = StopPointGrid( 'GCUT', 'GCUT', 'h', width=gcutWidth, pitch=gcutPitch, offset=gcutWidth/2)
        self.gcut1.addGridPoint( 0,                 False)
        self.gcut1.addGridPoint( stoppoint,         True)
        self.gcut1.addGridPoint( plOffset,          False)
        self.gcut1.addGridPoint( dcPitch-stoppoint, True)
        self.gcut1.addGridPoint( dcPitch,           False)

        self.pc = StopPointGrid( 'pc', 'polycon', 'h', width=pcWidth, pitch=pcPitch, offset=pcOffset)
        self.pc.addGridPoint( 0,                 False)
        self.pc.addGridPoint( stoppoint,         True)
        self.pc.addGridPoint( dcPitch//2,        False)
        self.pc.addGridPoint( dcPitch-stoppoint, True)
        self.pc.addGridPoint( dcPitch,           False)
        
        self.lisd = StopPointGrid( 'LISD', 'LISD', 'v', width=lisdWidth, pitch=m1Pitch, offset=m1Offset)
        self.lisd.addGridPoint( 0,                   False)
        self.lisd.addGridPoint( stoppoint,           True)
        self.lisd.addGridPoint( 2*m0Pitch,           False)
        self.lisd.addGridPoint( 4*m0Pitch-stoppoint, True)
        self.lisd.addGridPoint( 4*m0Pitch,           False)

        self.sdt = StopPointGrid( 'SDT', 'SDT', 'v', width=sdtWidth, pitch=m1Pitch, offset=m1Offset)
        self.sdt.addGridPoint( 0,                   False)
        self.sdt.addGridPoint( stoppoint,           True)
        self.sdt.addGridPoint( 2*m0Pitch,           False)
        self.sdt.addGridPoint( 4*m0Pitch-stoppoint, True)
        self.sdt.addGridPoint( 4*m0Pitch,           False)


    def addSegment( self, grid, netName, pinName, c, bIdx, eIdx):
        segment = grid.segment( netName, pinName, c, bIdx, eIdx)
        self.terminals.append( segment)
        return segment
        
    def addSegment1( self, grid, netName, pinName, bIdy, eIdy, bIdx, eIdx):
        segment1 = grid.segment1( netName, pinName, bIdy, eIdy, bIdx, eIdx)
        self.terminals.append( segment1)
        return segment1

    def m0Segment( self, netName, pinName, x0, x1, y): return self.addSegment( self.m0, netName, pinName, y, x0, x1)
    def m1Segment( self, netName, pinName, x, y0, y1): return self.addSegment( self.m1, netName, pinName, x, y0, y1)
    def m2Segment( self, netName, pinName, x0, x1, y): return self.addSegment( self.m2, netName, pinName, y, x0, x1)
    def m3Segment( self, netName, pinName, x, y0, y1): return self.addSegment( self.m3, netName, pinName, x, y0, y1)
    def plSegment( self, netName, pinName, x, y0, y1): return self.addSegment( self.pl, netName, pinName, x, y0, y1)
    def dcSegment( self, netName, pinName, x, y0, y1): return self.addSegment( self.dc, netName, pinName, x, y0, y1)
    def finSegment( self, netName, pinName, x0, x1, y): return self.addSegment( self.fin, netName, pinName, y, x0, x1)
    def activeSegment( self, netName, pinName, x0, x1, y): return self.addSegment( self.active, netName, pinName, y, x0, x1)
    def pselectSegment( self, netName, pinName, y0, y1, x0, x1): return self.addSegment1( self.pselect, netName, pinName, y0, y1, x0, x1)
    def nwellSegment( self, netName, pinName, y0, y1, x0, x1): return self.addSegment1( self.nwell, netName, pinName, y0, y1, x0, x1)
    def gcutSegment( self, netName, pinName, x0, x1, y): return self.addSegment( self.gcut, netName, pinName, y, x0, x1)
    def gcut1Segment( self, netName, pinName, x0, x1, y): return self.addSegment( self.gcut1, netName, pinName, y, x0, x1)
    def pcSegment( self, netName, pinName, x0, x1, y): return self.addSegment( self.pc, netName, pinName, y, x0, x1)
    def v0Segment( self, netName, pinName, y0, y1, x0, x1): return self.addSegment1( self.v0, netName, pinName, y0, y1, x0, x1)
    def lisdSegment( self, netName, pinName, x, y0, y1): return self.addSegment( self.lisd, netName, pinName, x, y0, y1)
    def sdtSegment( self, netName, pinName, x, y0, y1): return self.addSegment( self.sdt, netName, pinName, x, y0, y1)
    def v1Segment( self, netName, pinName, x0, x1, y): return self.addSegment( self.v1, netName, pinName, y, x0, x1)
    def v2Segment( self, netName, pinName, x0, x1, y): return self.addSegment( self.v2, netName, pinName, y, x0, x1)

    def unit( self, x, y):
######## Basic data #############
        m1Pitch = 54
        m1Offset = 37
        m1Width  = 18
        m2Pitch = 54
        m2Width = 18
        lisdWidth = 24
        sdtWidth = 24
        v0Width = 18
        v1Width = 18
        gcutWidth = 18
        v0Pitch = 36
        v_enclosure = 7
        poly_enclosure = 7
        plPitch = 54
        finPitch = 27
        finWidth = 7
        plWidth = 20
        plActive = 25 
        plActive_s = 29 
        pcWidth = 18 
        pc_gateExtension = 1 
        pc_activeDistance = 30 
        pcLength = (gate_u-1)*plPitch + plWidth + (2*pc_gateExtension)
        extension_x = (plPitch - plWidth)/2  
        extension_y = 0 
        K_space = extension_y // finPitch 
        fin_enclosure = 10
######## Derived from Basic data ###########
        finDummy = 4
        fin = int(round(fin_u + 2*finDummy))
        fin1 = int(round(fin_u + 1))
        gate = int(round(gate_u + 2)) 
        activeWidth_h = ((gate - 3)) * plPitch + (plActive * 2) + plWidth
        activeWidth1 = finPitch*fin_u
        activeWidth = finPitch*fin_u1
        activePitch = activeWidth1 + (2*finDummy + K_space)*finPitch + extension_y
        activeOffset = (activeWidth/2) + finDummy*finPitch - fin_enclosure
        pcOffset = activeOffset + pc_activeDistance + pcWidth/2 + activeWidth/2
        cont_no = (activeWidth//v0Pitch -1)
        pcPitch  = activePitch
        x_length = ((gate-1)*plPitch) + plWidth + extension_x
        y_length = fin * finPitch + extension_y
        y_total = y_length*y_cells
        m1Length = m2Width + (2*v_enclosure) + (m2Pitch*((fin_u+2)//2))
        m1PCLength = m2Width + (2*v_enclosure) + (m2Pitch*((fin_u+4)//2))
        m2_tracks = int(round(y_total/m2Pitch))

        SA = []
        SB = []
        DA = []
        DB = []
        GA = []
        GB = []
        for k in range(x_cells//2):
            if k%2 == 0:
                p = 0
            else:
                p = 4
            lS = 8*k + p
            lG = lS + 1
            lD = lS + gate_u
            SA.append(lS)
            GA.append(lG)
            DA.append(lD)
        for k in range(x_cells//2):
            if k%2 == 0:
                p = 4
            else:
                p = 0
            lS = 8*k + p
            lG = lS + 1
            lD = lS + gate_u
            SB.append(lS)
            GB.append(lG)
            DB.append(lD)
        #print (SA)  
                            
        for i in range(gate):
            uc.plSegment( 'g', 'NA', (i+(x*gate)), ((y*y_length)+((y-1)*extension_y)), (((1+y)*y_length)+(y*extension_y)))
            if i < (gate-1):                                                                 
                if i == 0 or i == gate_u: 
                    uc.lisdSegment( 'LISD', 'NA', (i+(x*gate)), (finDummy*finPitch - fin_enclosure + y*activePitch), (finDummy*finPitch - fin_enclosure + activeWidth + y*activePitch))
                    uc.sdtSegment( 'SDT', 'NA', (i+(x*gate)), (finDummy*finPitch - fin_enclosure + y*activePitch), (finDummy*finPitch - fin_enclosure + activeWidth + y*activePitch)) 
                    for j in range(cont_no):
                        uc.v0Segment( 'v0', 'NA', (finDummy*finPitch - fin_enclosure + j*v0Pitch + y*activePitch + v0Width), (finDummy*finPitch - fin_enclosure + j*v0Pitch + y*activePitch + 2*v0Width ),  (m1Offset - (m1Width/2) + i*m1Pitch + x*gate*plPitch), (m1Offset - (m1Width/2) + i*m1Pitch +x*gate*plPitch + v0Width) )
                else:
                    
                    uc.v0Segment( 'v0', 'NA', ( pcOffset - pcWidth/2 + y*activePitch), (pcOffset - pcWidth/2 + y*activePitch + v0Width ), (m1Offset - (m1Width/2) + i*m1Pitch + x*gate*plPitch), (m1Offset - (m1Width/2) + i*m1Pitch + x*gate*plPitch + v0Width) )
     
        for i in range(fin):  
            uc.finSegment( 'fin', 'NA', (((x-1)*extension_x)+ x*x_length), ((1+x)*(x_length)+x*extension_x), (i+(y*fin) + (2*K_space)*y))                   
       
        uc.gcutSegment( 'GCUT', 'NA', (((x-1)*extension_x)+ x*x_length), ((1+x)*(x_length)+x*extension_x), y) 
        if y == 0:
            uc.gcut1Segment( 'GCUT', 'NA', (((x-1)*extension_x)+ x*x_length), ((1+x)*(x_length)+x*extension_x), 0)
        uc.activeSegment( 'active', 'NA', (plActive_s+ x*(plPitch*gate)), ( activeWidth_h + plActive_s + x*(plPitch * gate)), y) 
        uc.pcSegment( 'PC', 'NA', ( plPitch - pc_gateExtension + x*(gate*plPitch)), (plPitch - pc_gateExtension + x*(gate*plPitch) + pcLength), y) 
        if x == x_cells -1 and y == y_cells -1:
            uc.pselectSegment( 'pselect', 'NA', 0, (((y+1)*y_length)+((y)*extension_y)), (((0-1)*extension_x)), ((1+x)*(x_length)+x*extension_x)) 
            uc.nwellSegment( 'nwell', 'NA', 0, (((y+1)*y_length)+((y)*extension_y)), (((0-1)*extension_x)), ((1+x)*(x_length)+x*extension_x))

##### Routing for Current Mirror  Load

############### M3 routing ###########################
        for i in range(3):
            if x == 0 and y_cells > 1 and i == 0:
                if y == 0:
                    uc.m3Segment( 'm3', 'S', (i+(x*gate)), ((m2Pitch*(finDummy//2-1)) - v_enclosure), ((y_cells-1)*m2Pitch*(K_space + fin//2) - v_enclosure + m1Length + (m2Pitch*(finDummy//2))))
                uc.v2Segment( 'v2', 'NA', ((i+x*gate)*m1Pitch + m1Offset - v1Width/2), ((i+x*gate)*m1Pitch + m1Offset + v1Width -   v1Width/2), (y*(m2_tracks //y_cells + K_space) + finDummy//2 + 1))

            if x == 0 and y_cells > 1 and i == 1:
                if y == 0:
                    uc.m3Segment( 'm3', 'DB', (i+(x*gate)), ((m2Pitch*(finDummy//2-1)) - v_enclosure), ((y_cells-1)*m2Pitch*(K_space + fin//2) - v_enclosure + m1Length + (m2Pitch*(finDummy//2))))
                uc.v2Segment( 'v2', 'NA', ((i+x*gate)*m1Pitch + m1Offset - v1Width/2), ((i+x*gate)*m1Pitch + m1Offset + v1Width -   v1Width/2), (y*(m2_tracks //y_cells + K_space) + finDummy//2 + 0))
                uc.v2Segment( 'v2', 'NA', ((i+x*gate)*m1Pitch + m1Offset - v1Width/2), ((i+x*gate)*m1Pitch + m1Offset + v1Width -   v1Width/2), (y*(m2_tracks //y_cells + K_space) + finDummy//2 + 3))

            if x == 0 and y_cells > 1 and i == 2:
                if y == 0:
                    uc.m3Segment( 'm3', 'DA', (i+(x*gate)), ((m2Pitch*(finDummy//2-1)) - v_enclosure), ((y_cells-1)*m2Pitch*(K_space + fin//2) - v_enclosure + m1Length + (m2Pitch*(finDummy//2))))
                uc.v2Segment( 'v2', 'NA', ((i+x*gate)*m1Pitch + m1Offset - v1Width/2), ((i+x*gate)*m1Pitch + m1Offset + v1Width -   v1Width/2), (y*(m2_tracks //y_cells + K_space) + finDummy//2 + 2))


            if x == 1 and y_cells > 1 and i == 2:
                if y == 0:
                    uc.m3Segment( 'm3', 'DB', (i+(x*gate)), ((m2Pitch*(finDummy//2-1)) - v_enclosure), ((y_cells-1)*m2Pitch*(K_space + fin//2) - v_enclosure + m1Length + (m2Pitch*(finDummy//2))))
                uc.v2Segment( 'v2', 'NA', ((i+x*gate)*m1Pitch + m1Offset - v1Width/2), ((i+x*gate)*m1Pitch + m1Offset + v1Width -   v1Width/2), (y*(m2_tracks //y_cells + K_space) + finDummy//2 + 3))

############### M2 routing ###########################
        for i in range((m2_tracks+1)):

            if i == (2*y*(m2_tracks //y_cells + K_space)):
                uc.m2Segment( 'm2', 'GND', (((x-1)*extension_x)+ x*x_length), ((1+x)*(x_length)+x*extension_x), i)

            if i == ((2*y+1)*(m2_tracks //y_cells + K_space)):
                uc.m2Segment( 'm2', 'VDD', (((x-1)*extension_x)+ x*x_length), ((1+x)*(x_length)+x*extension_x), i)

            if x_cells > 1 and x == 0 and i == (y*(m2_tracks //y_cells + K_space) + finDummy//2 + 0):
                uc.m2Segment( 'm2', 'DB', (m1Offset - m1Width/2 - v_enclosure), (m1Offset + m1Width/2 + v_enclosure + (x_cells*gate-2)*m1Pitch), i)

            if x_cells > 1 and x == 0 and i == (y*(m2_tracks //y_cells + K_space) + finDummy//2 + 1):
                uc.m2Segment( 'm2', 'S', (m1Offset - m1Width/2 - v_enclosure), (m1Offset + m1Width/2 + v_enclosure + (x_cells*gate-2)*m1Pitch), i)
         
     
            if x_cells > 1 and x == 0 and i == (y*(m2_tracks //y_cells + K_space) + finDummy//2 + 2):
                uc.m2Segment( 'm2', 'DA', (m1Offset - m1Width/2 - v_enclosure), (m1Offset + m1Width/2 + v_enclosure + (x_cells*gate-2)*m1Pitch), i)

            if x_cells > 1 and x == 0 and i == (y*(m2_tracks //y_cells + K_space) + finDummy//2 + 3):
                uc.m2Segment( 'm2', 'DB', (m1Offset - m1Width/2 - v_enclosure), (m1Offset + m1Width/2 + v_enclosure + (x_cells*gate-2)*m1Pitch), i)

################# M1 routing ######################       
        if (x_cells - 1 - x) == 0:
            if (y % 2) == 0:
                for i in DA:
                    uc.v1Segment( 'v1', 'NA', (i*m1Pitch + m1Offset - v1Width/2), (i*m1Pitch + m1Offset + v1Width -   v1Width/2), (y*(m2_tracks //y_cells + K_space) + finDummy//2 + 2))
                    uc.m1Segment( 'D', 'DA', i, ((m2Pitch*(finDummy//2-1)) - v_enclosure + y*m2Pitch*(K_space + fin//2) ), (y*m2Pitch*(K_space + fin//2) - v_enclosure + m1Length + (m2Pitch*(finDummy//2-1))))
                for i in DB:
                    uc.v1Segment( 'v1', 'NA', (i*m1Pitch + m1Offset - v1Width/2), (i*m1Pitch + m1Offset + v1Width -   v1Width/2), (y*(m2_tracks //y_cells + K_space) + finDummy//2 + 3))
                    uc.m1Segment( 'D', 'DB', i, ((m2Pitch*(finDummy//2-1)) - v_enclosure + y*m2Pitch*(K_space + fin//2) ), (y*m2Pitch*(K_space + fin//2) - v_enclosure + m1Length + (m2Pitch*(finDummy//2-1))))
                 
            else:
                for i in DA:
                    uc.v1Segment( 'v1', 'NA', (i*m1Pitch + m1Offset - v1Width/2), (i*m1Pitch + m1Offset + v1Width -   v1Width/2), (y*(m2_tracks //y_cells + K_space) + finDummy//2 + 3))
                    uc.m1Segment( 'D', 'DA', i, ((m2Pitch*(finDummy//2-1)) - v_enclosure + y*m2Pitch*(K_space + fin//2) ), (y*m2Pitch*(K_space + fin//2) - v_enclosure + m1Length + (m2Pitch*(finDummy//2-1))))
                for i in DB:
                    uc.v1Segment( 'v1', 'NA', (i*m1Pitch + m1Offset - v1Width/2), (i*m1Pitch + m1Offset + v1Width -   v1Width/2), (y*(m2_tracks //y_cells + K_space) + finDummy//2 + 2))
                    uc.m1Segment( 'D', 'DB', i, ((m2Pitch*(finDummy//2-1)) - v_enclosure + y*m2Pitch*(K_space + fin//2) ), (y*m2Pitch*(K_space + fin//2) - v_enclosure + m1Length + (m2Pitch*(finDummy//2-1))))
                                 

        if (x_cells - 1 - x) == 0:
            for i in GA:
                uc.v1Segment( 'v1', 'NA', (i*m1Pitch + m1Offset - v1Width/2), (i*m1Pitch + m1Offset + v1Width -   v1Width/2), (y*(m2_tracks //y_cells + K_space) + finDummy//2 + 0))
                uc.m1Segment( 'G', 'DB', i, (0 - v_enclosure + (m2Pitch*(finDummy//2-1)) + y*m2Pitch*(K_space + fin//2) ), (y*m2Pitch*(K_space + fin//2)+ (m2Pitch*(finDummy//2-1)) - v_enclosure + m1PCLength)) 
            for i in GB:
                uc.v1Segment( 'v1', 'NA', (i*m1Pitch + m1Offset - v1Width/2), (i*m1Pitch + m1Offset + v1Width -   v1Width/2), (y*(m2_tracks //y_cells + K_space) + finDummy//2 + 0))                
                uc.m1Segment( 'G', 'DB', i, (0 - v_enclosure + (m2Pitch*(finDummy//2-1)) + y*m2Pitch*(K_space + fin//2) ), (y*m2Pitch*(K_space + fin//2)+ (m2Pitch*(finDummy//2-1)) - v_enclosure + m1PCLength))

            for i in SA:
                uc.v1Segment( 'v1', 'NA', (i*m1Pitch + m1Offset - v1Width/2), (i*m1Pitch + m1Offset + v1Width -   v1Width/2), (y*(m2_tracks //y_cells + K_space) + finDummy//2 + 1))
                uc.m1Segment( 'S', 'S', i, ((m2Pitch*(finDummy//2-1)) - v_enclosure + y*m2Pitch*(K_space + fin//2) ), (y*m2Pitch*(K_space + fin//2) - v_enclosure + m1Length + (m2Pitch*(finDummy//2-1)))) 
            for i in SB:
                uc.v1Segment( 'v1', 'NA', (i*m1Pitch + m1Offset - v1Width/2), (i*m1Pitch + m1Offset + v1Width -   v1Width/2), (y*(m2_tracks //y_cells + K_space) + finDummy//2 + 1))
                uc.m1Segment( 'S', 'S', i, ((m2Pitch*(finDummy//2-1)) - v_enclosure + y*m2Pitch*(K_space + fin//2) ), (y*m2Pitch*(K_space + fin//2) - v_enclosure + m1Length + (m2Pitch*(finDummy//2-1)))) 
        
                     
                        
if __name__ == "__main__":
    fin_u1 = int(sys.argv[1])
    x_cells = int(sys.argv[2])
    y_cells = int(sys.argv[3])
    assert (x_cells%2) == 0
    gate_u = 2
    if fin_u1%2 != 0:
        fin_u = fin_u1 + 1
    else:
        fin_u = fin_u1 
    uc = UnitCell()

    for (x,y) in ( (x,y) for x in range(x_cells) for y in range(y_cells)):
        uc.unit( x, y)

    uc.computeBbox()

    with open( "./mydesign_dr_globalrouting.json", "wt") as fp:
        data = { 'bbox' : uc.bbox.toList(), 'globalRoutes' : [], 'globalRouteGrid' : [], 'terminals' : uc.terminals}
        fp.write( json.dumps( data, indent=2) + '\n')
