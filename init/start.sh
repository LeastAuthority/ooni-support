#!/bin/sh

MLABSIM_HOME='mlab1.nuq0t.measurement-lab.org'

source /etc/mlab/slice-functions
cd $SLICEHOME
# NOTE: oonib drops privilges if UID/GID are set in oonib.conf
$SLICEHOME/bin/oonib -c $SLICEHOME/oonib.conf &

if [ "$(hostname)" = "$MLABSIM_HOME" ]; then
    echo 'Starting mlabsim...'
    rm -vf $SLICEHOME/mlabsim.pid
    $SLICEHOME/bin/mlabsim --log-level DEBUG >> /home/mlab_ooni/mlabsim.log 2>&1 &
    echo $! > $SLICEHOME/mlabsim.pid
fi
