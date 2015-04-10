import funcVectorAlgebra



class readGeometry(object):
    
    def __init__(self,file_geom):

        self.file_geom=file_geom


    def read_beam_geometry(self):
        
        beam=[]
        for line in self.file_geom:
            
            coordinate = line.split()
            if coordinate[0] == 'NodeNo' and coordinate[1]=='X' and coordinate[2]=='Y' and coordinate[3]=='Z':
                print 'I cannot convert string to float'     
            else :
                
                beam.append((float(coordinate[1]),float(coordinate[2]),float(coordinate[3])))


        ''' add the halos segments and then transform the beam into line segments '''

        beam_segments = funcVectorAlgebra.segments(beam)

        beam_segments_halo = funcVectorAlgebra.add_halo(beam_segments)

        beam.insert(0,beam_segments_halo[0][0])

        beam.insert(len(beam),beam_segments_halo[-1][1])

        return beam


        
class BeamTranform(readGeometry):

    def __init__(self, input_file, input_file2,readGeometry):

        self.input_file = input_file
        self.input_file2 = input_file2
        self.readGeometry =readGeometry

    def read_translation(self):

        translation_applied = []
        #rotation_applied = []
        ''' fill the list with the points from the file and convert them to floats'''
        for line in self.input_file:

            displacement = line.split()
    
            if displacement[0]=='NodeNo' and displacement[1]=='dX' and displacement[2]=='dY' and displacement[3]=='dZ'  and displacement[7]=='Thx' and displacement[8]=='Thy' and displacement[9]=='Thz' :
                print 'I cannot convert string to float'
            else:

                translation_applied.append((float(displacement[1]),float(displacement[2]),float(displacement[3])))

        '''add the extrapolated translation values at the halos based on an average'''

        halo_translation_wing_root = 0.0
        halo_translation_wing_tip  = 2.0 * translation_applied[-1][2] - translation_applied[-2][2]

        ''' select the axis (FOR THIS CASE IN Z from translation_applied list) . Note: ADD  INDEPENDENT AXIS OF TRANSLATION FOR FUTURE TEST CASES'''

        translation_Z  = []

        
        for deform in translation_applied:
            translation_Z.append(deform[2])

        ''' add the halo movements at the wing root and the wing tip '''
        #print translation_Z
        translation_Z.insert(0,halo_translation_wing_root)
        translation_Z.insert(len(translation_Z),halo_translation_wing_tip)
        #print 'I am the translation   ', translation_Z
        
        ''' Apply the translation of beam and return the new beam'''
        beam_geom = self.readGeometry(self.input_file2)

        beam_stick = beam_geom.read_beam_geometry()
        #print 'this is the  beam stick    = ' , beam_stick
        for bum in beam_stick:
            print bum
        #new_beam_stick = beam_stick.read_beam_geometry()

        #print 'I am the beam stick    ' ,   new_beam_stick
        print '                                                         '
        print '                                                         '
        beam_geometry_translation = []

        for point in beam_stick:
            ind = beam_stick.index(point)
            beam_geometry_translation.append((point[0],point[1],point[2] + translation_Z[ind]))
        
        #print 'this         is          the              translated           beam ', beam_geometry_translation
        for bam in beam_geometry_translation:
            print bam
        print '                                                         '
        print '                                                         '
        return beam_geometry_translation


    def read_rotation(self):

        rotation_applied = []

        for line in self.input_file:

            angle = line.split()

            if angle[0]=='NodeNo' and angle[1]=='dX' and angle[2]=='dY' and angle[3]=='dZ'  and angle[7]=='Thx' and angle[8]=='Thy' and angle[9]=='Thz' :
                print 'I cannot convert string to float'
            
            else:

                rotation_applied.append((float(angle[7]),float(angle[8]),float(angle[9])))


        ''' interpolate the angle at the at the projection point '''        
           
        return rotation_applied





