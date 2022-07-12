import enum


class Status(enum.Enum):
    Upcoming = 'Upcoming'
    Scheduled = 'Scheduled'
    Executed = 'Executed'
    Running = 'Running'


class Frequency(enum.Enum):
    Hourly = 'Hourly'
    Daily = 'Daily'
    Weekly = 'Weekly'
    Monthly = 'Monthly'
    Once = 'Once'


class Trigger(enum.Enum):
    Manual = 'Manual'
    Scheduled = 'Scheduled'


class HistoryStatus(enum.Enum):
    Successful = 'Successful'
    Failed = 'Failed'


class ReviewStatus(enum.Enum):
    Approved = 'Approved'
    Review = 'Review'
    Rejected = 'Rejected'
    Draft = 'Draft'
