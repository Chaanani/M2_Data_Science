document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('loadTopicsBtn').addEventListener('click', loadTopics);
});

function loadTopics() {
    fetch('/ws/topics')
        .then(response => response.json())
        .then(topics => {
            const topicsDiv = document.getElementById('topics');
            topicsDiv.innerHTML = '<h2>Topics:</h2>';
            topicsDiv.innerHTML = '<h6> Si vous voulez voir les liens de topics, il faut cliquer sur le topic que vous souhaitez le voir:</h6>';
            topics.forEach(topic => {
                const topicElement = document.createElement('p');
                topicElement.textContent = topic;
                topicElement.onclick = () => loadItems(topic);
                topicsDiv.appendChild(topicElement);
            });
        })
        .catch(error => console.error('Erreur:', error));
}

function loadItems(topic) {
    fetch(`/ws/topic/${topic}`)
        .then(response => response.json())
        .then(items => {
            const itemsDiv = document.getElementById('items');
            itemsDiv.innerHTML = `<h2>Items pour ${topic}:</h2>`;
            Object.entries(items).forEach(([item, urls]) => {
                itemsDiv.innerHTML += `<p>${item}: ${urls.join(', ')}</p>`;
            });
        })
        .catch(error => console.error('Erreur:', error));
}

