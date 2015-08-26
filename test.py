try:

    def bounds_to_coords(maxlat,maxlng,minlat,minlng):
        global new_lats, new_lons,new_coords,coordinates
        new_lats=[]
        new_lngs=[]
        new_coords={}
        coordinates=[]
        x=float(maxlat)
        y=float(maxlng)
        min_x=float(minlat)
        min_y=float(minlng)
        while(x>=min_x):
	   x-=0.005
	   new_lats.append(x)

        while (y>=min_y):
	   y-=0.005
	   new_lngs.append(y)
     
     
        for i in range(len(new_lats)):
           for j in range(len(new_lngs)):
               new_coords ={'lat': new_lats[i],'lng':new_lngs[j]}
               coordinates.append(new_coords)
        
        return coordinates


except Exception as e:
    print e
