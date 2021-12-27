import numpy as np

from helpers.data import DataLoader
from helpers.day_solution_class import SolutionTemplate
from scipy.spatial import ConvexHull
from scipy.spatial.distance import cdist


class Solution(SolutionTemplate):

    def __init__(self):
        self.total_beacons_set = None
        self.beacon_locations = {}
        dataloader = DataLoader(19)
        current_scanner = 0
        beacons = []
        beacons_all = []
        debug = False
        file = dataloader.debug_file if debug else dataloader.input_file
        with open(file, 'r') as f:
            for line in f:
                line = line.rstrip()
                if 'scanner' in line:
                    current_scanner = int(line.split(' ')[2])
                    beacons = []
                elif "," in line:
                    x, y, z = map(int, line.split(","))
                    beacons.append([x, y, z])
                elif not line:
                    beacons_all.append(beacons)
            beacons_all.append(beacons)
        self.data = beacons_all

    def first_solution(self) -> int:
        total_beacons = self.data[0]
        beacon_locations = {0: np.array([0,0,0])}
        beacons_increasing = True
        while beacons_increasing:
            beacon_count = len(total_beacons)
            for ib in range(1, len(self.data)):
                if ib in beacon_locations.keys(): continue
                total_beacons_np = np.array(total_beacons)
                current_beacon = np.array(self.data[ib])
                overlapping_points_dist = self.find_overlapping_points_dist(current_beacon, total_beacons_np)

                overlapping_points_ip = set()
                for points in overlapping_points_dist:
                    if len(self.find_overlapping_points_with_angles(total_beacons_np, current_beacon, *points)) >= 12:
                        overlapping_points_ip = self.find_overlapping_points_with_angles(
                            total_beacons_np, current_beacon, *points)
                        subs_total = []
                        subs_current = []
                        for i in overlapping_points_ip:
                            subs_total.append(list(total_beacons_np[i[0]]))
                            subs_current.append(list(current_beacon[i[1]]))
                        c, R, t = self.umeyama(np.array(subs_current), np.array(subs_total))
                        if ib not in beacon_locations.keys(): beacon_locations[ib] = t
                        transformed_current = current_beacon @ R + t
                        for r in transformed_current:
                            ri = np.round(r).astype('int').tolist()
                            if ri not in total_beacons:
                                total_beacons.append(ri)
                        break
                else:
                    print(f'no matching beacons found for beacon {ib}')
            beacons_increasing = beacon_count < len(total_beacons)
        self.total_beacons_set = total_beacons
        self.beacon_locations = beacon_locations
        return len(total_beacons)

    def find_overlapping_points_dist(self, current_beacon, total_beacons_np):
        os = self.find_overlapping_dist(total_beacons_np, current_beacon)
        return os

    def first_answer(self) -> int:
        return 419

    def second_solution(self) -> int:
        print(self.beacon_locations)
        total_beacon_set_np = np.array(list(map(list, self.beacon_locations.values())))
        max_dist = 0
        for i in range(len(total_beacon_set_np)):
            for j in range(len(total_beacon_set_np)):
                dist = np.linalg.norm(total_beacon_set_np[i] - total_beacon_set_np[j], ord=1)
                if dist > max_dist: max_dist = dist
        return max_dist

    def second_answer(self) -> int:
        return 13210

    @staticmethod
    def find_overlapping_dist(c0, c1):
        matching = set()
        if len(c0.shape) == 1:
            c0 = c0[:, np.newaxis]
            c1 = c1[:, np.newaxis]
        for i in range(len(c0)):
            rd0 = set(np.linalg.norm(c0 - c0[i], ord=1, axis=1).astype('int'))
            for j in range(len(c1)):
                rd1 = set(np.linalg.norm(c1 - c1[j], ord=1, axis=1).astype('int'))
                if len(rd0.intersection(rd1)) >= 12:
                    matching.add((i, j))
        return matching

    @staticmethod
    def find_overlapping_points_with_angles(c0, c1, p0, p1) -> {(int, int)}:
        matching = {(p0, p1)}
        for i in range(len(c0)):
            rd0 = set(np.abs(np.dot(c0 - c0[p0], c0[i] - c0[p0])).astype('int'))
            for j in range(len(c1)):
                rd1 = set(np.abs(np.dot(c1 - c1[p1], c1[j] - c1[p1])).astype('int'))
                if len(rd0.intersection(rd1)) >= 12:
                    matching.add((i, j))
        return matching

    @staticmethod
    def umeyama(P, Q):
        assert P.shape == Q.shape
        n, dim = P.shape

        centeredP = P - P.mean(axis=0)
        centeredQ = Q - Q.mean(axis=0)

        C = np.dot(np.transpose(centeredP), centeredQ) / n

        V, S, W = np.linalg.svd(C)
        d = (np.linalg.det(V) * np.linalg.det(W)) < 0.0

        if d:
            S[-1] = -S[-1]
            V[:, -1] = -V[:, -1]

        R = np.dot(V, W)

        varP = np.var(P, axis=0).sum()
        c = 1 / varP * np.sum(S)  # scale factor

        t = Q.mean(axis=0) - P.mean(axis=0).dot(c * R)

        return c, R, t


if __name__ == "__main__":
    solution = Solution()
    print(solution.first_solution())
    print(solution.second_solution())
