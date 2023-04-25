from visualizations import ptolemy_bound_vector_space, ptolemy_bound_vector_space_triple, ptolemy_bound_pivot_space


# ---------------------------- Execution ----------------------------
if __name__ == '__main__':
    q = (47, 38)
    p1 = (40, 50)
    p2 = (60, 50)
    p3 = (38, 60)
    distance = 'euclidean'
    ptolemy_bound_vector_space(q, p=p1, s=p2, distance=distance)
    # ptolemy_bound_vector_space_triple(q=q, p1=p1, p2=p2, p3=p3, distance=distance)
    ptolemy_bound_pivot_space(q, p1, p2, distance=distance)
