if "testfile.txt.a" in listfiles();
	removefile("testfile.txt.a")
if "testfile.txt.b" in listfiles();
	removefile("testfile.txt.b")

myfile.ABopenfile("testfile.txt", True)
try:
	def write_with_thread(str):
		def write():
			myfile.writeat(str,0)

		return write
		
	Thread_1_write = write_with_thread("S1234E")
	Thread_2_write = write_with_thread("s1234e")

	createthread(Thread_1_write)
	createthread(Thread_2_write)

	assert ('S' == myfile.readat(1,0))
	myfile.close()
except:
	log("threading failed")
	myfile.close()