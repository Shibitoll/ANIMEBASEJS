// src/pages/HomePage.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import AnimeCard from '../components/AnimeCard';
import FeaturedSection from '../components/FeaturedSection';
import './HomePage.css'; 

const API_URL = 'http://127.0.0.1:8000/api/v1/anime/';

const HomePage = () => {
    const [animeList, setAnimeList] = useState([]);
    const [featuredAnime, setFeaturedAnime] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        axios.get(API_URL)
            .then(response => {
                const data = response.data;
                setAnimeList(data);
                
                const featured = data.find(a => a.is_featured);
                setFeaturedAnime(featured);
                
                setLoading(false);
            })
            .catch(err => {
                console.error("Помилка завантаження даних API:", err);
                setError("Не вдалося завантажити дані. Переконайтеся, що Django API запущено.");
                setLoading(false);
            });
    }, []);
    
    const recentReleases = animeList.slice(0, 3);
    const popularAnime = animeList.slice(0, 6); 

    if (loading) {
        return <div className="loading-container">Завантаження...</div>;
    }

    if (error) {
         return <div className="error-container" style={{ color: 'red', textAlign: 'center' }}>{error}</div>;
    }

    return (
        <div className="home-page-container">
            {/* 1. Рекомендовані аніме */}
            {featuredAnime && <FeaturedSection anime={featuredAnime} />}
            
            {/* 2. Нещодавно додані*/}
            <section className="anime-section">
                <h2>✨ Нещодавно додані</h2>
                <div className="cards-grid">
                    {recentReleases.map(anime => ( 
                        <AnimeCard key={anime.id} anime={anime} />
                    ))}
                </div>
            </section>
            
            <hr className="divider" />

            {/* 3.Популярні аніме*/}
            <section className="anime-section">
                <h2>🔥 Популярні аніме</h2>
                <div className="cards-grid">
                    {popularAnime.map(anime => (
                        <AnimeCard key={anime.id} anime={anime} />
                    ))}
                </div>
            </section>
        </div>
    );
};

export default HomePage;