from numpy.linalg import det
from Point import Point
class MPPVertices:
    def __init__(self):
        pass
    #change from point to xy coordinates
    def get_points(self,BW_points):
        BW_vertices=[]
        for i in range(1,BW_points.shape[0]):
            #P=Point()
            PK=BW_points[i]
            arr=[PK.x,PK.y,PK.type]
            BW_vertices.append(arr)
        return BW_vertices


    def get_sign(self,vl,BW,vk):
        mat=[vl,BW,vk]
        sign=det(mat)
        return sign

    def Is_vertix(self,BW_point):
        BW_points=self.get_points(BW_point)
        #print(BW_points)
        V0=BW_points[0]
        VL=V0
        Bc=V0
        Wc=V0
        xy_cordinates=[V0[0],V0[1]]
        MPP_vertices=[xy_cordinates]

        for i in range (1,BW_points.__len__()-1):
            V1=BW_points[i]
            Vk=V1
            sign=self.get_sign(VL,Wc,Vk)
            sign2=self.get_sign(VL,Bc,Vk)
            if sign>0:
                VL=Wc
                Wc=VL
                Bc=VL

            elif ((sign<=0)&(sign2>=0)):
                xy_cordinates=[Vk[0],Vk[1]]
                MPP_vertices.append(xy_cordinates)
                if Vk[2]==1: #1 is white
                    Wc=Vk
                elif Vk[2]==0: #0 is black
                    Bc=Vk
            elif(sign2<0):
                VL=Bc
                Wc=VL
                Bc=VL
        return MPP_vertices






