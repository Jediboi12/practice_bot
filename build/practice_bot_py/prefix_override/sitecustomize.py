import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/jedidiah-sanusi/practice_bot/install/practice_bot_py'
