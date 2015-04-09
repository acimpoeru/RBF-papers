import funcVectorAlgebra





class readFiles(object):
    
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
                
        return beam


        
class BeamTranform(object):

    def __init__(self, input_file):

        self.input_file = input_file


    def translation(self):

        translation_applied = []
        #rotation_applied = []
        
        for line in self.input_file:

            displacement = line.split()
    
            if displacement[0]=='NodeNo' and displacement[1]=='dX' and displacement[2]=='dY' and displacement[3]=='dZ'  and displacement[7]=='Thx' and displacement[8]=='Thy' and displacement[9]=='Thz' :
                print 'I cannot convert string to float'
            else:

                translation_applied.append((float(displacement[1]),float(displacement[2]),float(displacement[3])))
                
        return translation_applied

    def rotation(self):

        rotation_applied = []

        for line in self.input_file:

            angle = line.split()

            if angle[0]=='NodeNo' and angle[1]=='dX' and angle[2]=='dY' and angle[3]=='dZ'  and angle[7]=='Thx' and angle[8]=='Thy' and angle[9]=='Thz' :
                print 'I cannot convert string to float'
            
            else:

                rotation_applied.append((float(angle[7]),float(angle[8]),float(angle[9])))
        
        return rotation_applied

