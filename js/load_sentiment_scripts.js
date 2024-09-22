function include(file) {
 
    let script = document.createElement('script');
    script.src = file;
    script.type = 'text/javascript';
    script.defer = true;
 
    document.getElementsByTagName('head').item(0).appendChild(script);
 
}

path_to_scripts = "../../visualizations/scripts/entities-sentiment/"
const chartScripts = [
    'positive_articles_count.js',
    'neutral_articles_count.js',
    'negative_articles_count.js',
    'top_positive_articles.js',
    'top_negative_articles.js',
    'sentiment_trends.js',
    'articles_grouped_by_entity_and_sentiment.js',
    'entities_by_year.js',
    'top_entity_by_sentiment.js'
];

for (let script of chartScripts){
    script = path_to_scripts + script;
    include(script);
}

