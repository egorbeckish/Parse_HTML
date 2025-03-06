from utils import *


# homeworks = get_homeworks()
homeworks = get_homeworks('files_html')
# show_homeworks(homeworks, 'March')
df = create_df(homeworks)
print(df)