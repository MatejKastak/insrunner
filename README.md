# Insrunner

This program gives you ability to run instruction and check registers/memory.
It provides convenient interface to work with assembly. Inspired by [https://github.com/hugsy/cemu/](cemu).

## Dependencies

This program depends on radare2 and r2pipe. And also reasonable [python](http://stfupy3.org/).
That's it.

## Building

```
git clone https://github.com/MatejKastak/insrunner && cd insrunner

# Make sure you have installed r2 https://github.com/radare/radare2
# For arm64 you may need keystone plugin for r2
# Install keystone for your distribution
# r2pm -i keystone
# If this approach does not work please try GAS backend eg. -b gas

# Create virtualenv
virtualenv --python=/bin/python3.7 venv
source venv/bin/activate
pip install -r requirements.txt

# Start your assembly journey
python insrunner

# Fingers crossed, nothing breaks at this point
```

## TODO

Resolve all todos in sources, obviously.

Formatted printing, for example multiple bases and widths of registers/memory

## Author

Matej Kastak
