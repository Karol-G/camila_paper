from multiprocessing import Pool

global_pool = None
global_pool_results = []


def init_pool(processes):
    global global_pool
    global global_pool_results
    if global_pool is not None:
        raise RuntimeError("Pool was already initialized.")
    global_pool = Pool(processes)
    global_pool_results = []
    return global_pool, global_pool_results


def get_pool(processes=1):
    global global_pool
    global global_pool_results
    if global_pool is None:
        global_pool = Pool(processes)
        global_pool_results = []
    return global_pool, global_pool_results


def get_results():
    global global_pool_results
    results = [i.get() for i in global_pool_results]
    global_pool_results = []
    return results


def close_pool():
    global global_pool
    get_results()
    global_pool.close()
    global_pool.join()



