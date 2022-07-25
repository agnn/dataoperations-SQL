import logging as lg

# logging file to create basic config file.

lg.basicConfig(filename= "F:\\ineuron FSDS\dataoperation\log.txt",
               level=lg.DEBUG,
               format='[%(asctime)s - %(levelname)s - "Module" %(module)s] : %(message)s')
lg.info("info")

