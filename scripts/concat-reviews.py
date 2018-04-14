import pandas as pd
import os


# Concatenate reviews per user
def concat_reviews(df_reviews=None, id_column=None):
    assert id_column in ('user_id', 'item_id')
    for _, (id_value, df) in enumerate(df_reviews.groupby(id_column)):
        yield (id_value, ' '.join(df.review_text.tolist()))


def main():
    # Load reviews from disk
    print('Loading reviews...')
    df_reviews = pd.read_csv('../data/reviews.csv')

    # Remove records with empty or missing reviews
    print('Processing reviews...')
    df_reviews.dropna(subset=['review_text'], inplace=True)
    df_reviews['review_text'] = df_reviews.review_text.astype(str)

    print('Concatenating user reviews...')
    df_user_reviews = pd.DataFrame(
        concat_reviews(df_reviews, id_column='user_id'),
        columns=['user_id', 'review_text']
    )
    df_user_reviews.to_csv(os.path.join('../data/user-reviews.csv'), index=False)
    del df_user_reviews

    print('Concatenating item reviews...')
    df_item_reviews = pd.DataFrame(
        concat_reviews(df_reviews, id_column='item_id'),
        columns=['item_id', 'review_text']
    )
    df_item_reviews.to_csv(os.path.join('../data/item-reviews.csv'), index=False)

    print('Finished')


if __name__ == '__main__':
    main()
