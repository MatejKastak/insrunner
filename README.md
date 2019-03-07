# Insrunner

This program gives you ability to run instruction and check registers/memory.
It provides convenient interface to work with assembly.

## Dependencies

This program depends on radare2 and r2pipe. And also reasonable [python](http://stfupy3.org/).
That's it.

## Building

```
git clone https://github.com/MatejKastak/insrunner && cd insrunner

# Make sure you have installed r2 https://github.com/radare/radare2

# If you want create virtualenv
sudo pip install r2pipe

# Start your assembly journey
./main.py

# Fingers crossed, nothing breaks at this point
```

## TODO

Resolve all todos in sources, obviously.

Formatted printing, for example multiple bases and widths of registers/memory

## Author

Matej Kastak
