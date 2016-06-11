OLD_FILE='./media-chunk/sample.3gp'
NEW_FILE='./media-chunk/sample.wav'

rm $NEW_FILE

echo "hello"

ffmpeg -i $OLD_FILE $NEW_FILE

echo "hello2"