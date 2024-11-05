def sortTheStudents(score: List[List[int]], k: int) -> List[List[int]]:
        """
        matrix: [[std_01_score_01, std_01_score_02, std_01_score_03, ...],
                 [std_02_score_01, std_02_score_02, std_02_score_03, ...],
                 ....]
        k : the i-th row
        + distinct scores

        ! abnormal case:  k > 
        """
        dict_idRow_score = {}
        sorted_matrix = []
        #
        list_max_scores = []
        for id_row, std_scores in enumerate(score):
            dict_idRow_score[std_scores[k]] = id_row
            list_max_scores.append(std_scores[k])
        #
        list_max_scores.sort(reverse=True)
        #
        for max_score in list_max_scores:
            sorted_matrix.append(score[dict_idRow_score[max_score]])
        return sorted_matrix