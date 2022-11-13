import time


class Timer:
    """This timer simple timer record current time in when it is initialised and print du duration between inisialisation and destrucion during it's destrucion"""
    name: str
    begin_time: float
    end_time: float
    is_timer_ended: bool = False
    DISPLAY_BEGIN_END_TIMES: bool = False

    def __init__(self, name: str):
        self.name = name
        if self.DISPLAY_BEGIN_END_TIMES:
            print(f"{self.name} timer started at : {self.display_time()}")
        self.begin_time = time.time()

    def __del__(self) -> float:
        if not self.is_timer_ended:
            self.stop_timer()
        if self.DISPLAY_BEGIN_END_TIMES:
            print(f"{self.name} timer ended at : {self.display_time()}")
        # Keep in float to get full precission
        timer_duration: float = self.end_time - self.begin_time
        print(
            f"{self.name} à duré : {int(timer_duration * 1000)} milisecondes\n")  # Convert in int to display the number whole
        return timer_duration

    def get_current_duration(self) -> float:
        return time.time() - self.begin_time

    def stop_timer(self):
        self.end_time = time.time()
        self.is_timer_ended = True

    def display_time(self) -> str:
        return time.strftime("%H:%M %Ss", time.gmtime())
