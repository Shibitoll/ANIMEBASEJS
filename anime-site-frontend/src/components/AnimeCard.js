// src/components/AnimeCard.js
import React from 'react';
import './AnimeCard.css'; 

const AnimeCard = ({ anime }) => {
    const genreList = anime.genres.split(',').map(g => g.trim());

    return (
        <div className="anime-card" data-status={anime.status.toLowerCase()}>
            <div className="card-image-container">
                <img src={anime.image_url} alt={anime.title} className="card-image" />
                <div className="status-tag">{anime.status}</div>
                
                {}
                {anime.status === 'Ongoing' && (
                    <div className="watch-overlay">
                        <button className="watch-btn">▶ Watch</button>
                    </div>
                )}
            </div>
            <div className="card-info">
                <h3 className="card-title">{anime.title}</h3>
                <div className="card-meta">
                    <span className="rating">⭐ {anime.rating}</span>
                    <span>• {anime.year}</span>
                    <span>• {anime.episodes}</span>
                </div>
                <div className="card-genres">
                    {}
                    {genreList.slice(0, 2).map((g, index) => (
                         <span key={index} className="genre-tag">{g}</span>
                    ))}
                </div>
                <p className="card-description">{anime.description.substring(0, 80)}...</p>
            </div>
        </div>
    );
};

export default AnimeCard;