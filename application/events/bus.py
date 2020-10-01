from pydispatch import Dispatcher


class Bus(Dispatcher):
    _events_ = ['new_report']
