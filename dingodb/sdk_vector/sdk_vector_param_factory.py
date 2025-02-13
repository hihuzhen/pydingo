#!/usr/bin/python3

import dingosdk


class SDKParamFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_flat_param(index_type: str, flat_param_dict: dict) -> dingosdk.FlatParam:
        assert index_type == "flat"

        return dingosdk.FlatParam(
            flat_param_dict["dimension"], flat_param_dict["metricType"]
        )

    @staticmethod
    def create_ivf_flat_param(
        index_type: str, ivf_flat_param_dict: dict
    ) -> dingosdk.IvfFlatParam:
        assert index_type == "ivf_flat"

        param = dingosdk.IvfFlatParam(
            ivf_flat_param_dict["dimension"],
            ivf_flat_param_dict["metricType"],
        )
        param.ncentroids = ivf_flat_param_dict["ncentroids"]

        return param

    @staticmethod
    def create_ivf_pq_param(
        index_type: str, ivf_pq_param_dict: dict
    ) -> dingosdk.IvfPqParam:
        assert index_type == "ivf_pq"

        param = dingosdk.IvfPqParam(
            ivf_pq_param_dict["dimension"],
            ivf_pq_param_dict["metricType"],
        )
        param.ncentroids = ivf_pq_param_dict["ncentroids"]
        param.nsubvector = ivf_pq_param_dict["nsubvector"]
        param.bucket_init_size = ivf_pq_param_dict["bucketInitSize"]
        param.bucket_max_size = ivf_pq_param_dict["bucketMaxSize"]
        param.nbits_per_idx = ivf_pq_param_dict["nbitsPerIdx"]

        return param

    @staticmethod
    def create_hnsw_param(index_type: str, hnsw_param_dict: dict) -> dingosdk.HnswParam:
        assert index_type == "hnsw"

        param = dingosdk.HnswParam(
            hnsw_param_dict["dimension"],
            hnsw_param_dict["metricType"],
            hnsw_param_dict["maxElements"],
        )
        param.ef_construction = hnsw_param_dict["efConstruction"]
        param.nlinks = hnsw_param_dict["nlinks"]

        return param

    @staticmethod
    def create_diskann_param(
        index_type: str, diskann_param_dict: dict
    ) -> dingosdk.DiskAnnParam:
        assert index_type == "diskann"

        param = dingosdk.DiskAnnParam(
            diskann_param_dict["dimension"],
            diskann_param_dict["metricType"],
            diskann_param_dict["valueType"],
        )

        param.search_list_size = diskann_param_dict["searchListSize"]
        param.max_degree = diskann_param_dict["maxDegree"]

        return param

    @staticmethod
    def create_brute_param(
        index_type: str, brute_param_dict: dict
    ) -> dingosdk.BruteForceParam:
        assert index_type == "brute"

        return dingosdk.BruteForceParam(
            brute_param_dict["dimension"],
            brute_param_dict["metricType"],
        )


    @staticmethod
    def create_binary_flat_param(index_type: str, binary_flat_param_dict: dict) -> dingosdk.BinaryFlatParam:
        assert index_type == "binary_flat"

        return dingosdk.BinaryFlatParam(
            binary_flat_param_dict["dimension"], binary_flat_param_dict["metricType"]
        )

    @staticmethod
    def create_binary_ivf_flat_param(
        index_type: str, binary_ivf_flat_param_dict: dict
    ) -> dingosdk.BinaryIvfFlatParam:
        assert index_type == "binary_ivf_flat"

        param = dingosdk.BinaryIvfFlatParam(
            binary_ivf_flat_param_dict["dimension"],
            binary_ivf_flat_param_dict["metricType"],
        )
        param.ncentroids = binary_ivf_flat_param_dict["ncentroids"]

        return param