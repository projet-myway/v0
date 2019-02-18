import unittest

from Station import Station
import datetime
import numpy as np


class Test_Station(unittest.TestCase):

    def test_init(self):

        stop_id, stop_name, stop_desc, stop_lat, stop_lon = \
            2377, "République", "Av de la République - 75111", 48.86761748653104, 2.3638195214331654
        s = Station(stop_id, stop_name, stop_desc, stop_lat, stop_lon)
        self.assertEqual(2377, s.stop_id)
        self.assertEqual("République", s.stop_name)

    def test_compute_duration_to_every_neighbour(self):

        stop_id, stop_name, stop_desc, stop_lat, stop_lon = \
            2377, "République", "Av de la République - 75111", 48.86761748653104, 2.3638195214331654
        s = Station(stop_id, stop_name, stop_desc, stop_lat, stop_lon)

        set_of_date_w = {datetime.date(2019, 1, 21), datetime.date(2019, 1, 22), datetime.date(2019, 1, 23),
                         datetime.date(2019, 1, 24), datetime.date(2019, 1, 25)}
        set_of_date_w_e = {datetime.date(2019, 1, 26), datetime.date(2019, 1, 27)}

        t_w = []
        t_w.append(datetime.time(0, 5))
        t_w.append(datetime.time(15, 30))
        t_w.append(datetime.time(16, 30))
        t_w.append(datetime.time(17, 30))

        t_w_e = []
        t_w_e.append(datetime.time(0, 30))
        t_w_e.append(datetime.time(13, 30))
        t_w_e.append(datetime.time(17, 30))
        t_w_e.append(datetime.time(19, 30))

        for t in t_w:
            # 1197630 route_id
            s.add_trip(1197630, set_of_date_w, t, 2294, datetime.timedelta(minutes=1))

        for t in t_w_e:
            s.add_trip(1197630, set_of_date_w_e, t, 2294, datetime.timedelta(minutes=1))

        t_w = []
        t_w.append(datetime.time(0, 45))
        t_w.append(datetime.time(15, 40))
        t_w.append(datetime.time(16, 40))
        t_w.append(datetime.time(17, 40))
        t_w.append(datetime.time(17, 50))

        t_w_e = []
        t_w_e.append(datetime.time(0, 40))
        t_w_e.append(datetime.time(13, 40))
        t_w_e.append(datetime.time(17, 40))
        t_w_e.append(datetime.time(19, 20))
        t_w_e.append(datetime.time(19, 50))
        t_w_e.append(datetime.time(19, 40))

        for t in t_w:
            # 1197630 route_id
            s.add_trip(1197630, set_of_date_w, t, 2310, datetime.timedelta(minutes=1))

        for t in t_w_e:
            # 1197630 route_id
            s.add_trip(1197630, set_of_date_w_e, t, 2310, datetime.timedelta(minutes=10))


        d = s.compute_duration_to_every_neighbour(datetime.date(2019, 1, 21), datetime.time(15, 00))
        # 30 +1 wait + duration
        self.assertEqual({2294: 31, 2310: 41}, d)

        d = s.compute_duration_to_every_neighbour(datetime.date(2019, 1, 26), datetime.time(15, 00))
        self.assertEqual({2294: 151, 2310: 170}, d)

        d = s.compute_duration_to_every_neighbour(datetime.date(2019, 1, 26), datetime.time(20, 00))
        # print(d)
        self.assertEqual({2294: 271, 2310: 290}, d)

    def test_compute_duration_to_every_neighbour_2(self):

        stop_id, stop_name, stop_desc, stop_lat, stop_lon = \
            2377, "République", "Av de la République - 75111", 48.86761748653104, 2.3638195214331654
        s = Station(stop_id, stop_name, stop_desc, stop_lat, stop_lon)

        set_of_date_w = {datetime.date(2019, 1, 21), datetime.date(2019, 1, 22), datetime.date(2019, 1, 23),
                         datetime.date(2019, 1, 24),
                         datetime.date(2019, 1, 25)}
        set_of_date_w_e = {datetime.date(2019, 1, 26), datetime.date(2019, 1, 27)}

        t_w = []
        t_w.append(datetime.time(0, 5))
        t_w.append(datetime.time(15, 30))
        t_w.append(datetime.time(16, 30))
        t_w.append(datetime.time(17, 30))

        t_w_e = []
        t_w_e.append(datetime.time(0, 30))
        t_w_e.append(datetime.time(13, 30))
        t_w_e.append(datetime.time(17, 30))
        t_w_e.append(datetime.time(19, 30))

        for t in t_w:
            # 1197630 route_id
            s.add_trip(1197630, set_of_date_w, t, 2294, datetime.timedelta(minutes=1))

        for t in t_w_e:
            # 1197630 route_id
            s.add_trip(1197630, set_of_date_w_e, t, 2294, datetime.timedelta(minutes=1))

        # s.sort_schedule()

        d = s.compute_duration_to_every_neighbour(datetime.date(2019, 1, 21), datetime.time(15, 00))
        self.assertEqual({2294: 31}, d)

        d = s.compute_duration_to_every_neighbour(datetime.date(2019, 1, 21), datetime.time(15, 30))
        self.assertEqual({2294: 1}, d)

        d = s.compute_duration_to_every_neighbour(datetime.date(2019, 1, 21), datetime.time(15, 31))
        # 59 minutes wait+1 trip
        self.assertEqual({2294: 60}, d)

        d = s.compute_duration_to_every_neighbour(datetime.date(2019, 1, 21), datetime.time(23, 0))
        self.assertEqual({2294: 66}, d)

        d = s.compute_duration_to_every_neighbour(datetime.date(2019, 1, 25), datetime.time(23, 00))
        self.assertEqual({2294: 91}, d)

    def test_compute_duration_to_every_neighbour_No_Train_today_but_tomorrow(self):

        stop_id, stop_name, stop_desc, stop_lat, stop_lon = \
            2377, "République", "Av de la République - 75111", 48.86761748653104, 2.3638195214331654
        s = Station(stop_id, stop_name, stop_desc, stop_lat, stop_lon)

        set_of_date_w_e = {datetime.date(2019, 1, 26), datetime.date(2019, 1, 27)}

        t = []
        t.append(datetime.time(00, 30))
        t.append(datetime.time(1, 30))
        t.append(datetime.time(2, 30))

        t.append(datetime.time(13, 30))
        t.append(datetime.time(17, 30))
        t.append(datetime.time(19, 30))

        for t_i in t:
            # 1197630 route_id
            s.add_trip(1197630, set_of_date_w_e, t_i, 2294, datetime.timedelta(minutes=1))


        d = s.compute_duration_to_every_neighbour(datetime.date(2019, 1, 25), datetime.time(22, 00))
        print(d)
        self.assertEqual({2294: 151}, d)

        d = s.compute_duration_to_every_neighbour(datetime.date(2019, 1, 25), datetime.time(21, 59))
        self.assertEqual({2294: 152}, d)

        d = s.compute_duration_to_every_neighbour(datetime.date(2019, 1, 25), datetime.time(0, 0))
        self.assertEqual({2294: 1471}, d)

        d = s.compute_duration_to_every_neighbour(datetime.date(2019, 1, 24), datetime.time(22, 0))
        self.assertEqual({2294: 1591}, d)

        d = s.compute_duration_to_every_neighbour(datetime.date(2019, 1, 23), datetime.time(22, 0))
        self.assertEqual({2294: 3031}, d)

    def test_compute_duration_to_every_neighbour_No_Train_at_all(self):

        stop_id, stop_name, stop_desc, stop_lat, stop_lon = \
            2377, "République", "Av de la République - 75111", 48.86761748653104, 2.3638195214331654
        s = Station(stop_id, stop_name, stop_desc, stop_lat, stop_lon)

        set_of_date_w_e = {datetime.date(2019, 1, 26), datetime.date(2019, 1, 27)}

        t = []
        t.append(datetime.time(00, 30))
        t.append(datetime.time(1, 30))
        t.append(datetime.time(2, 30))

        t.append(datetime.time(13, 30))
        t.append(datetime.time(17, 30))
        t.append(datetime.time(19, 30))

        for t_i in t:
            # 1197630 route_id
            s.add_trip(1197630, set_of_date_w_e, t_i, 2294, datetime.timedelta(minutes=1))

        self.assertEqual(datetime.date(2019, 1, 27), s.max_date)

        d = s.compute_duration_to_every_neighbour(datetime.date(2019, 1, 28), datetime.time(22, 00))

        self.assertEqual(None, d)


if __name__ == '__main__':
    unittest.main()
