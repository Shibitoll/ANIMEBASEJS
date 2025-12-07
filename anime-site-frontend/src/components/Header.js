// src/components/Header.js
import React from 'react';
import './Header.css';

const Header = () => {
    return (
        <header className="main-header">
            <div className="header-content">
                <div className="logo">
                    AnimeBase
                </div>
                <nav className="main-nav">
                    <a href="/" className="nav-link active">Головна</a>
                    <a href="/favorite" className="nav-link">Улюблені</a>
                </nav>
                <div className="search-and-login">
                    <div className="search-bar">
                        <input type="text" placeholder="Пошук аніме..." />
                        <span className="search-icon">🔍</span>
                    </div>
                    <button className="login-btn">
                        <span>👤Зареєструватись</span>
                    </button>
                    <button className="login-btn">
                        <span>👤Увійти</span>
                    </button>
                </div>
            </div>
        </header>
    );
};

export default Header;