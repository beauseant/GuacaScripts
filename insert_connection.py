import pandas as pd
import numpy as np
import argparse
import configparser
from lib.Database import DB

if __name__ == "__main__":


	parser = argparse.ArgumentParser()

	parser.add_argument('-f','--file', help='el csv con las conexiones a insertar', required='True',)
	parser.add_argument('-c','--config', help='el fichero de configuracion a utilizar', required='True',)

	args = parser.parse_args()

	cfg = configparser.ConfigParser()


	if not cfg.read([ args.config ]):
		print ('Archivo de configuracion no encontrado :(')
	else:
		try:
			nombre 		= cfg.get ( 'DATABASE','nombre')
			passwd 		= cfg.get ( 'DATABASE','passwd')
			usuario		= cfg.get ( 'DATABASE','usuario')
			servidor	= cfg.get ( 'DATABASE','servidor')
		except:
			exit ()




	df = pd.read_csv(args.file, header=0).replace(np.nan, '', regex=True)

	listDict = df.to_dict('records')

	guacaDB = DB ( servidor, usuario, passwd, nombre)

	
	for connection in listDict:
		print ('.')
		guacaDB.insertConnection (connection)

	
	