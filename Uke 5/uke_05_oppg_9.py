def draw_haiku_frame(a, b, c):
    størrelse = max(len(a), len(b), len(c))
    frame_1 = ("@ " + " "*(størrelse - len(a)) + a + " @")
    frame_2 = ("@ " + " "*(størrelse - len(b)) + b + " @")
    frame_3 = ("@ " + " "*(størrelse - len(c)) + c + " @")
    frame_4 = ("@"*(størrelse+4))
    frame = frame_4+"\n"+frame_1+"\n"+frame_2+"\n"+frame_3+"\n"+frame_4
    
    return frame
print (draw_haiku_frame("hei", "på", "dittelidei"))