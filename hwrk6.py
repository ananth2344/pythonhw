blog_views = [150, 800, 2500, 600, 1200, 450, 3000]

total_views = 0
trending_count = 0

for views in blog_views:
    total_views += views  
    if views > 1000:
        print("Trending")
        trending_count += 1
    elif views >= 500:
        print("Average")
    else:
        print("Low Traffic")
print("\nTotal Views:", total_views)
print("Number of Trending Posts:", trending_count)
