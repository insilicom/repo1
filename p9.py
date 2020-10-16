exam_st_date = (11, 12, 2014)
print(type(exam_st_date[0]))
mon = exam_st_date[0]
day = exam_st_date[1]
year = exam_st_date[2]
print("The examination will start from : "+str(mon)+"/"+str(day)+"/"+str(year))
print("The examination will start from : %i/%i/%i"%exam_st_date)
