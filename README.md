**Metrics collection script**

Python script for for retrieving information on running processes and system utilization.

**Getting Started**

It can be used on Linux servers or Docker container. 

$`git clone https://github.com/solonkoolesya/metrics.git`

**Usage**

____As a plain script:____

You need only _metric.py_ file. Make sure that python3 is installed on your machine.
Make sure that file is executable.

Run:

`$ pip install psutil argparse` 

`$ cd metrics`

Help:

`$ ./metrics.py -h`

For retrieving cpu info:

`$ ./metrics.py -cpu`

For retrieving memory info:

`$ ./metrics.py -mem`

****_In the Docker continer:_****

It haven't pythont and pip packages installed in your OS. 
For building image run on working directory:

`$ docker build -t mymetr .`

For retrieving cpu info run:

`$ docker run -it --rm --pid=host mymetr python metrics.py -cpu`

For retrieving memory info run:

`$ docker run -it --rm --pid=host mymetr python metrics.py -mem`