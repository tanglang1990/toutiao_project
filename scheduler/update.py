"""
编写各种更新任务的函数
"""
from offline.update_article import UpdateArticle


def update_article_profile():
    """文章画像的定时更新逻辑
    :return:
    """
    ua = UpdateArticle()
    sentence_df = ua.merge_article_data()
    if sentence_df.rdd.collect():
        rank, idf = ua.generate_article_label(sentence_df)
        articleProfile = ua.get_article_profile(rank, idf)
        ua.compute_article_similar(articleProfile)