#!/bin/python3

import math
import librosa
import numpy as np
import os

def existance(chemin):
	
	while True:
		if os.path.exists(chemin):
			break
		else:
			print(f"Le fichier {chemin} n'existe pas!!")
			chemin = input('\n\n\n	+veuillez entrer un fichier existant:\n		---->')
	return chemin

def ent_audio(audio):
	#***-initialisation***#
	tot = 0	      	      #
	somme_amp = {}	      #
	H = 0		      #
	#*********************#
	
	# calcul les valeurs d'amplitude
	compt_amp = np.histogram(audio, bins=256)[0]
    

	

	# transferer les amplitudes en dict
	for amplitude, compt in enumerate(compt_amp):
		somme_amp[amplitude] = compt
	
	
	#calcul des somme d'amplitude
	
	
	for k,v in somme_amp.items():
		somme_amp[k] = somme_amp.get(k, 0) + v
		tot += v
	
	P ={}
	for k, v in somme_amp.items():
		P[k] = v/tot
	
	for k,v in P.items():
		if v > 0:
			H += -(v*math.log2(v))
	
	return  H

print('-------------------------------------------------------------------------------------------')
print('					BIENVENUE!!!')
print('-------------------------------------------------------------------------------------------\n\n\n\n\n')

while True:

	chemin = input('entrez votre audio: ')
	chemin = existance(chemin)
	y, sr = librosa.load(chemin, sr=None)
	H_aud = ent_audio(y)
		#piano			#piano		#piano		#piano			#violon		#violon		#violon		#violon
	ref = [10.64394477380757,7.8436567116427165,9.50242719018764,8.745825171294264,10.144029307479478,9.818221720732446,10.87443698394696,9.009361576752141]

	H_j = abs(H_aud - ref[0])
	j = 0
	for i in range(7):
		if abs(H_aud-ref[i+1]) < H_j:
			H_j = abs(H_aud-ref[i+1])
			j = i

	if j < 4:
		print('---------------------------------------je crois que c est du piano---------------------------------------')
		print('\n')
		print('					║░█░█░║░█░█░█░║░█░█░║')
		print('					║░█░█░║░█░█░█░║░█░█░║')
		print('					║░║░║░║░║░║░║░║░║░║░║')
		print('					╚═╩═╩═╩═╩═╩═╩═╩═╩═╩═╝')
	else:
		print('---------------------------------------je crois que c est du violon---------------------------------------')
		print('_¶¶¶¶¶¶')
		print('_¶¶¶¶¶¶¶ ¶') 
		print('_¶11¶¶1¶¶¶')
		print('_1¶1¶1¶¶¶¶')
		print('¶¶¶1¶¶¶¶¶¶')
		print('_¶¶¶1¶¶¶¶1') 
		print('___1¶1¶¶¶1') 
		print('____1¶¶¶¶¶1')
		print('_____¶¶¶¶¶¶')
		print('______¶¶¶¶¶¶')
		print('______1¶¶¶¶¶¶')
		print('_______¶¶¶¶¶¶1')
		print('________¶¶¶¶¶¶1')
		print('_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶') 
		print('_________¶¶¶¶¶¶¶1111¶¶¶¶¶') 
		print('_______¶¶¶¶¶¶¶¶¶1______¶¶¶1') 
		print('_____1¶¶¶__¶¶¶¶¶¶1______1¶¶1')
		print('____1¶¶1___1¶¶¶¶¶¶1______1¶¶')
		print('____¶¶1_____¶¶¶¶¶¶¶1______¶¶¶')
		print('____¶¶1______¶¶¶¶¶¶¶______1¶¶')
		print('____1¶1______1¶¶¶¶¶¶¶_____1¶¶')
		print('_____¶¶_______¶¶¶¶¶¶¶¶_____¶¶')
		print('_____¶¶¶_______¶¶¶¶¶¶¶1___¶¶¶')
		print('______¶¶¶______1¶¶¶¶¶¶¶___1¶¶')
		print('_______¶¶¶1_____¶¶1111¶¶___¶¶1')
		print('________1¶¶¶1____111111¶¶¶¶¶¶¶')
		print('__________1¶¶¶____¶1¶111¶__¶¶¶¶')
		print('____________¶¶¶_1¶¶¶1111¶¶1¶¶1¶¶1____') 
		print('_____________¶¶¶¶1_¶¶¶¶¶¶¶11¶__¶¶¶¶¶¶1')
		print('______________¶¶¶¶__¶¶¶111¶_¶¶1_¶¶11¶¶1')
		print('______________1¶11¶__¶1¶1¶1¶_1¶¶¶¶___¶¶¶')
		print('______________1¶¶_1¶_1¶11111¶_________¶¶¶¶') 
		print('_____________1¶¶___¶1_¶11111¶1__________¶¶¶')
		print('___________1¶¶¶1¶¶¶¶__1¶¶¶¶¶¶¶___________1¶¶')
		print('____________¶¶1_1¶¶____¶¶¶¶¶¶¶________11__¶¶1')
		print('____________1¶¶_________1¶¶¶¶¶1____1¶¶¶¶¶¶¶¶¶')
		print('____________1¶¶___________¶¶¶¶1___¶¶¶¶¶¶¶¶¶¶¶')
		print('____________1¶¶____________¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶')
		print('____________¶¶1_____________¶¶¶1_¶¶¶¶¶¶¶¶¶¶¶¶')
		print('____________1¶¶______________¶¶¶1¶¶¶¶¶¶¶¶¶¶¶ ')
		print('_____________¶¶¶_____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶1 ')
		print('______________¶¶¶_____________¶¶¶¶¶¶¶¶¶¶¶¶  ')
		print('_______________¶¶¶1___________1¶¶¶¶¶¶¶¶1  ')
		print('_______________11¶¶¶111_____111¶¶¶¶¶1 ')
		print('___________________1¶¶¶¶¶¶¶¶¶¶¶11')
	x = False
	while x == False:
		continuer = input('\n\n 	voulez-vous continuer:\n		----> ')
		if continuer.lower() in ['oui','continuer']:
			x = True
		elif continuer.lower() in ['non','fermer']:
			x = 'arreter'
			break
		else:
			print('\n\n				entrez une commande valide!!!')
	if x == 'arreter':
		break
		
print('\n\n\n')
print('-------------------------------------------------------------------------------------------')
print('					Au Revoir...')
print('-------------------------------------------------------------------------------------------\n\n\n\n\n')

