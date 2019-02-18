import unittest
import datetime
import Network


class Test_Network(unittest.TestCase):


    def test_One_route_5_compute_shortest_path_with_weight(self):

        r = Network.Network("Input/RATP_GTFS_METRO_5")
        date_and_time = datetime.datetime.strptime('20190321 15:25', '%Y%m%d %H:%M')

        parcours, duration = r.compute_shortest_path("Place d\'Italie", "République", date_and_time)
        print("\n")
        print(parcours, duration)
        ref = [(2403, 'transfer', 0), (2136, '5', 3), (2521, '5', 4), (2206, '5', 6), (2437, '5', 8), (2112, '5', 9),
               (2164, '5', 10), (2445, '5', 12), (2310, '5', 13), (2377, '5', 15)]
        # [("Place d'Italie", 'transfer', 0),
        #    ('Campo-Formio', '5', 3),
        #    ('Saint-Marcel', '5', 4),
        #    ("Gare d'Austerlitz", '5', 6),
        #    ('Quai de la Rapée', '5', 8),
        #    ('Bastille', '5', 9),
        #    ('Bréguet-Sabin', '5', 10),
        #    ('Richard-Lenoir', '5', 12),
        #    ('Oberkampf', '5', 13),
        #    ('République', '5', 15)]
        self.assertEqual(ref, parcours)
        self.assertEqual(15, duration)

        time = datetime.datetime.strptime('20190324 22:25', '%Y%m%d %H:%M')
        parcours, duration = r.compute_shortest_path("Place d\'Italie", "République", time)
        print("\n")
        print(parcours, duration)
        ref = [(2403, 'transfer', 0), (2136, '5', 2), (2521, '5', 3), (2206, '5', 4), (2437, '5', 6), (2112, '5', 8),
               (2164, '5', 9), (2445, '5', 10), (2310, '5', 11), (2377, '5', 13)]
        # [("Place d'Italie", 'transfer', 0),
        #        ('Campo-Formio', '5', 2),
        #        ('Saint-Marcel', '5', 3),
        #        ("Gare d'Austerlitz", '5', 4),
        #        ('Quai de la Rapée', '5', 6),
        #        ('Bastille', '5', 8),
        #        ('Bréguet-Sabin', '5', 9),
        #        ('Richard-Lenoir', '5', 10),
        #        ('Oberkampf', '5', 11),
        #        ('République', '5', 13)]
        self.assertEqual(ref, parcours)
        self.assertEqual(13, duration)  # 12 sur le site RATP

        time = datetime.datetime.strptime('20190324 23:25', '%Y%m%d %H:%M')
        parcours, duration = r.compute_shortest_path("République", "Place d\'Italie", time)
        print("\n")
        print(parcours, duration)
        ref = [(2377, 'transfer', 0), (1767, 'transfer', 0), (1843, '5', 4), (1700, '5', 5), (2008, '5', 6),
               (2063, '5', 7), (1759, '5', 9), (1951, '5', 11), (1641, '5', 12), (2017, '5', 13), (1793, '5', 16),
               (2403, 'transfer', 16)]
        # [('République', 'transfer', 0),
        #        ('République', 'transfer', 0),
        #        ('Oberkampf', '5', 4),
        #        ('Richard-Lenoir', '5', 5),
        #        ('Bréguet-Sabin', '5', 6),
        #        ('Bastille', '5', 7),
        #        ('Quai de la Rapée', '5', 9),
        #        ("Gare d'Austerlitz", '5', 11),
        #        ('Saint-Marcel', '5', 12),
        #        ('Campo-Formio', '5', 13),
        #        ("Place d'Italie", '5', 16),
        #        ("Place d'Italie", 'transfer', 16)]
        self.assertEqual(ref, parcours)
        self.assertEqual(16, duration)

    def test_One_route_4_compute_shortest_path_with_weight(self):
        r = Network.Network("Input/RATP_GTFS_METRO_4")
        time = datetime.datetime.strptime('20190321 15:25', '%Y%m%d %H:%M')

        parcours, duration = r.compute_shortest_path("Réaumur-Sébastopol", "Montparnasse-Bienvenue", time)
        print("\n")
        print(parcours, duration)
        ref = [(1764, 'transfer', 0), (1934, '4', 2), (1855, '4', 3), (1964, '4', 4), (1975, '4', 5), (1729, '4', 7),
               (1845, '4', 8), (1721, '4', 9), (1733, '4', 10), (1731, '4', 11), (1824, '4', 13)]
        # [('Réaumur-Sébastopol', 'transfer', 0),
        #        ('Etienne Marcel', '4', 2),
        #        ('Les Halles', '4', 3),
        #        ('Châtelet', '4', 4),
        #        ('Cité', '4', 5),
        #        ('Saint-Michel', '4', 7),
        #        ('Odéon', '4', 8),
        #        ('Saint-Germain des Prés', '4', 9),
        #        ('Saint-Sulpice', '4', 10),
        #        ('Saint-Placide', '4', 11),
        #        ('Montparnasse-Bienvenue', '4', 13)]
        self.assertEqual(ref, parcours)
        self.assertEqual(13, duration)

        time = datetime.datetime.strptime('20190324 22:25', '%Y%m%d %H:%M')

        parcours, duration = r.compute_shortest_path("Réaumur-Sébastopol", "Montparnasse-Bienvenue", time)
        print("\n")
        print(parcours, duration)
        ref = [(1764, 'transfer', 0), (1934, '4', 1), (1855, '4', 2), (1964, '4', 3), (1975, '4', 4), (1729, '4', 5),
               (1845, '4', 6), (1721, '4', 7), (1733, '4', 9), (1731, '4', 10), (1824, '4', 11)]
        # [('Réaumur-Sébastopol', 'transfer', 0),
        #        ('Etienne Marcel', '4', 1),
        #        ('Les Halles', '4', 2),
        #        ('Châtelet', '4', 3),
        #        ('Cité', '4', 4),
        #        ('Saint-Michel', '4', 5),
        #        ('Odéon', '4', 6),
        #        ('Saint-Germain des Prés', '4', 7),
        #        ('Saint-Sulpice', '4', 9),
        #        ('Saint-Placide', '4', 10),
        #        ('Montparnasse-Bienvenue', '4', 11)]
        self.assertEqual(ref, parcours)
        self.assertEqual(11, duration)

        time = datetime.datetime.strptime('20190324 23:25', '%Y%m%d %H:%M')
        parcours, duration = r.compute_shortest_path("Montparnasse-Bienvenue", "Réaumur-Sébastopol", time)
        print("\n")
        print(parcours, duration)

        ref = [(1824, 'transfer', 0), (2363, 'transfer', 0), (2442, '4', 6), (2411, '4', 7), (2466, '4', 8),
               (2312, '4', 9), (2472, '4', 10), (2230, '4', 12), (2219, '4', 13), (2322, '4', 14), (2259, '4', 15),
               (2374, '4', 16), (1764, 'transfer', 16)]
        # [('Montparnasse-Bienvenue', 'transfer', 0),
        #        ('Montparnasse-Bienvenue', 'transfer', 0),
        #        ('Saint-Placide', '4', 6),
        #        ('Saint-Sulpice', '4', 7),
        #        ('Saint-Germain des Prés', '4', 8),
        #        ('Odéon', '4', 9),
        #        ('Saint-Michel', '4', 10),
        #        ('Cité', '4', 12),
        #        ('Châtelet', '4', 13),
        #        ('Les Halles', '4', 14),
        #        ('Etienne Marcel', '4', 15),
        #        ('Réaumur-Sébastopol', '4', 16),
        #        ('Réaumur-Sébastopol', 'transfer', 16)]
        self.assertEqual(ref, parcours)
        self.assertEqual(16, duration)

    def test_Two_routes_4_5_compute_shortest_path_with_weight(self):
        r = Network.Network(*["Input/RATP_GTFS_METRO_4", "Input/RATP_GTFS_METRO_5"])

        time = datetime.datetime.strptime('20190321 15:25', '%Y%m%d %H:%M')

        parcours, duration = r.compute_shortest_path("Château d'Eau", "Jacques-Bonsergent", time)
        print(parcours, duration)
        ref = [(2153, 'transfer', 0), (2208, '4', 1), (2076, 'transfer', 3), (1898, '5', 5)]
        # [("Château d'Eau", 'transfer', 0),
        #        ("Gare de l'Est (Verdun)", '4', 1),
        #        ("Gare de l'Est (Verdun)", 'transfer', 3),
        #        ('Jacques-Bonsergent', '5', 5)]
        self.assertEqual(ref, parcours)
        self.assertEqual(5, duration)

        time = datetime.datetime.strptime('20190321 15:25', '%Y%m%d %H:%M')

        parcours, duration = r.compute_shortest_path("Jacques-Bonsergent", "Porte de Clignancourt", time)
        print(parcours, duration)
        ref = [(1898, 'transfer', 0), (2294, 'transfer', 0), (2125, '5', 3), (2208, 'transfer', 5), (2212, '4', 7),
               (2110, '4', 9), (2152, '4', 10), (2535, '4', 11), (2478, '4', 12), (2420, '4', 14),
               (1742, 'transfer', 14)]
        # [('Jacques-Bonsergent', 'transfer', 0),
        #        ('Jacques-Bonsergent', 'transfer', 0),
        #        ("Gare de l'Est (Verdun)", '5', 3),
        #        ("Gare de l'Est (Verdun)", 'transfer', 5),
        #        ('Gare du Nord', '4', 7),
        #        ('Barbès-Rochechouart', '4', 9),
        #        ('Château Rouge', '4', 10),
        #        ('Marcadet-Poissonniers', '4', 11),
        #        ('Simplon', '4', 12),
        #        ('Porte de Clignancourt', '4', 14),
        #        ('Porte de Clignancourt', 'transfer', 14)]
        self.assertEqual(ref, parcours)
        self.assertEqual(14, duration)

    def test_All_Subway_routes_compute_shortest_path_with_weight(self):
        l_routes = ["1", "2", "3", "3b", "4", "5", "6", "7", "7b", "8", "9", "10", "11", "12", "13", "14"]
        s = "Input/RATP_GTFS_METRO_"
        arg = [s + l for l in l_routes]

        r = Network.Network(*arg)

        time = datetime.datetime.strptime('20190321 15:25', '%Y%m%d %H:%M')

        parcours, duration = r.compute_shortest_path("Château d'Eau", "Jacques-Bonsergent", time)
        print(parcours, duration)
        ref = [(2153, 'transfer', 0), (2208, '4', 1), (2076, 'transfer', 3), (1898, '5', 5)]
        # [("Château d'Eau", 'transfer', 0), ("Gare de l'Est (Verdun)", '4', 1),
        #        ("Gare de l'Est (Verdun)", 'transfer', 3), ('Jacques-Bonsergent', '5', 5)]
        self.assertEqual(ref, parcours)
        self.assertEqual(5, duration)

        time = datetime.datetime.strptime('20190321 15:25', '%Y%m%d %H:%M')

        parcours, duration = r.compute_shortest_path("Jacques-Bonsergent", "Porte de Clignancourt", time)
        print("\n")
        print(parcours, duration)
        ref = [(1898, 'transfer', 0), (2294, 'transfer', 0), (2125, '5', 3), (2208, 'transfer', 5), (2212, '4', 7),
               (2110, '4', 9), (2152, '4', 10), (2535, '4', 11), (2478, '4', 12), (2420, '4', 14),
               (1742, 'transfer', 14)]
        # [('Jacques-Bonsergent', 'transfer', 0), ('Jacques-Bonsergent', 'transfer', 0),
        #    ("Gare de l'Est (Verdun)", '5', 3), ("Gare de l'Est (Verdun)", 'transfer', 5), ('Gare du Nord', '4', 7),
        #    ('Barbès-Rochechouart', '4', 9), ('Château Rouge', '4', 10), ('Marcadet-Poissonniers', '4', 11),
        #    ('Simplon', '4', 12), ('Porte de Clignancourt', '4', 14), ('Porte de Clignancourt', 'transfer', 14)]

        self.assertEqual(ref, parcours)
        self.assertEqual(14, duration)

        parcours, duration = r.compute_shortest_path("Pont de Sèvres", "Saint-Fargeau", time)
        print("\n")
        print(parcours, duration)
        ref = [(1804, 'transfer', 0), (2088, '9', 4), (1884, '9', 5), (1747, '9', 7), (1936, '9', 9), (1816, '9', 10),
               (1814, '9', 11), (1899, '9', 13), (1762, '9', 14), (1917, '9', 15), (1708, '9', 17), (1637, '9', 18),
               (1895, '9', 20), (2043, '9', 21), (1946, '9', 23), (1730, '9', 24), (1819, '9', 26), (1715, '9', 27),
               (1890, '9', 29), (1972, '9', 30), (1702, '9', 31), (1712, '9', 32), (2001, '9', 34), (1678, '9', 35),
               (1647, '9', 37),
               (2527, 'transfer', 37), (2376, 'transfer', 39), (2389, '3', 40), (2471, '3', 42),
               (2395, '3', 43), (2205, '3', 45), (2539, 'transfer', 47),
               (2393, '3B', 49), (2463, '3B', 50),
               (1718, 'transfer', 50)]
        # [('Pont de Sèvres', 'transfer', 0), ('Billancourt', '9', 4), ('Marcel Sembat', '9', 5),
        #    ('Porte de Saint-Cloud', '9', 7), ('Exelmans', '9', 9), ('Michel-Ange-Molitor', '9', 10),
        #    ('Michel-Ange-Auteuil', '9', 11), ('Jasmin', '9', 13), ('Ranelagh', '9', 14), ('La Muette', '9', 15),
        #    ('Rue de la Pompe (Avenue Georges Mandel)', '9', 17), ('Trocadéro', '9', 18), ('Iéna', '9', 20),
        #    ('Alma-Marceau', '9', 21), ('Franklin-Roosevelt', '9', 23), ('Saint-Philippe du Roule', '9', 24),
        #    ('Miromesnil', '9', 26), ('Saint-Augustin', '9', 27), ('Havre-Caumartin', '9', 29),
        #    ("Chaussée d'Antin (La Fayette)", '9', 30), ('Richelieu-Drouot', '9', 31),
        #    ('Grands Boulevards', '9', 32), ('Bonne Nouvelle', '9', 34), ('Strasbourg-Saint-Denis', '9', 35),
        #    ('République', '9', 37), ('République', 'transfer', 37), ('République', 'transfer', 39),
        #    ('Parmentier', '3', 40), ('Rue Saint-Maur', '3', 42), ('Père-Lachaise', '3', 43), ('Gambetta', '3', 45),
        #    ('Gambetta', 'transfer', 47),
        #    ('Pelleport', '3B', 49), ('Saint-Fargeau', '3B', 50),
        #    ('Saint-Fargeau', 'transfer', 50)]

        self.assertEqual(ref, parcours)
        self.assertEqual(50, duration)


if __name__ == '__main__':
    unittest.main()
