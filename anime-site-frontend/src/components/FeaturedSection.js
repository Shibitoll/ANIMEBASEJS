// src/components/FeaturedSection.js
import React from 'react';
import './FeaturedSection.css';

const FeaturedSection = ({ anime }) => {
    if (!anime) return null;

    const genres = anime.genres.split(',').map(g => g.trim()); 

    return (
        <div className="featured-section" style={{ backgroundImage: `url(${anime.image_url})` }}>
            <div className="featured-overlay">
                <div className="featured-content">
                    <div className="tags">
                        <span className="tag featured">Featured</span>
                        <span className="tag completed">{anime.status}</span>
                    </div>
                    <h1>{anime.title}</h1>
                    <p className="description">{anime.description}</p> 
                    <div className="meta-details">
                        <span>⭐ {anime.rating}</span>
                        <span>• {anime.year}</span>
                        <span>• {anime.episodes}</span>
                        {}
                        <span>• {genres.join(', ')}</span> 
                    </div>
                    <div className="action-buttons">
                        <button className="watch-now-btn">▶ Watch Now</button>
                        <button className="more-info-btn">ⓘ More Info</button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default FeaturedSection;