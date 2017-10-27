#!/bin/bash
#synchronise tous les repertoires necessaires de dumbo vers tim. C'est ici qu'il faut modifier les fichiers a synchroniser
# derniere modif par aymeric le 5 avril 2013 : j'exclu le repertoire partage/mediatheque
NOW=$(date +"%Y_%m_%d")

REPERTOIRESAVLOCAL="/home/pi/Photos/"
REPERTOIREDISTANT="/partage/Aymeric/Bricolage/Photomaton/SauvegardePhotos/"
#LOG="/home/exploit/log/Sv_Vers_Tim_$NOW.log.txt"
#SCRIPT="/opt/exploitation"
#REPERTOIREPARTAGE="/partage"
#REPERTOIREPARTAGEDISTANT="/Volume_1/FS"

HOST="shrek"
ping -q -c5 $HOST > /dev/null

if [ $? -eq 0 ]
  then
rsync -avz $REPERTOIRESAVLOCAL aymeric@$HOST:$REPERTOIREDISTANT

#echo "Sauvegarde Hebdomadaire vers TIM : Demarrage" | mail -s "[SHREK] Duplication des donnees"  -t aymeric.Defossez@gmail.com

#$SCRIPT/synchro_ftp.sh $REPERTOIRESAVLOCALDUJOUR $REPERTOIREDISTANT # > $LOG
#echo "Sauvegarde Hebdomadaire vers TIM : Duplication de la sauvegarde du jour effectuee." | mail -s "[SHREK] Duplication des donnees"  -t aymeric.Defossez@gmail.com

#$SCRIPT/synchro_ftp.sh $REPERTOIREPARTAGE $REPERTOIREPARTAGEDISTANT # >> $LOG

#echo "Sauvegarde Hebdomadaire vers TIM effectuee." | mail -s "[SHREK] Duplication des donnees"  -t aymeric.Defossez@gmail.com
echo "Termine!"

fi

