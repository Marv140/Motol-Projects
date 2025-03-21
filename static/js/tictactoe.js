document.addEventListener('DOMContentLoaded', () => {
    // Game state
    const board = document.getElementById('board');
    const winMessage = document.getElementById('win-message');
    const currentPlayerDisplay = document.getElementById('current-player');
    const restartButton = document.getElementById('restart-button');
    const xScoreDisplay = document.getElementById('x-score');
    const oScoreDisplay = document.getElementById('o-score');
    const drawsDisplay = document.getElementById('draws');
    
    const BOARD_SIZE = 15;
    const WIN_CONDITION = 5; // 5 in a row to win
    let currentPlayer = 'X';
    let gameBoard = Array(BOARD_SIZE).fill().map(() => Array(BOARD_SIZE).fill(''));
    let gameActive = true;
    
    // Score tracking
    let scores = {
        X: 0,
        O: 0,
        draws: 0
    };
    
    // Initialize the board
    function initializeBoard() {
        board.innerHTML = '';
        
        for (let row = 0; row < BOARD_SIZE; row++) {
            for (let col = 0; col < BOARD_SIZE; col++) {
                const cell = document.createElement('div');
                cell.classList.add('cell');
                cell.dataset.row = row;
                cell.dataset.col = col;
                cell.addEventListener('click', () => handleCellClick(row, col));
                board.appendChild(cell);
            }
        }
    }
    
    // Handle cell click
    function handleCellClick(row, col) {
        // If game is not active or cell is already filled, ignore the click
        if (!gameActive || gameBoard[row][col] !== '') return;
        
        // Update the game board
        gameBoard[row][col] = currentPlayer;
        
        // Update the UI
        updateCell(row, col);
        
        // Check for win or draw
        if (checkWin(row, col)) {
            endGame(`Hráč ${currentPlayer} vyhrál!`);
            updateScores(currentPlayer);
        } else if (checkDraw()) {
            endGame('Remíza!');
            updateScores('draw');
        } else {
            // Switch player
            currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
            currentPlayerDisplay.textContent = currentPlayer;
            currentPlayerDisplay.className = currentPlayer === 'X' ? 
                'player-icon player-x' : 'player-icon player-o';
        }
    }
    
    // Update cell appearance
    function updateCell(row, col) {
        const cell = document.querySelector(`.cell[data-row="${row}"][data-col="${col}"]`);
        cell.textContent = gameBoard[row][col];
        cell.classList.add(gameBoard[row][col].toLowerCase());
    }
    
    // Check for win
    function checkWin(row, col) {
        const directions = [
            [0, 1],  // horizontal
            [1, 0],  // vertical
            [1, 1],  // diagonal down-right
            [1, -1]  // diagonal down-left
        ];
        
        const player = gameBoard[row][col];
        
        for (const [dx, dy] of directions) {
            let count = 1;
            let winningCells = [[row, col]]; // Start with the current cell
            
            // Check in both directions
            for (const direction of [1, -1]) {
                let r = row + direction * dx;
                let c = col + direction * dy;
                
                while (
                    r >= 0 && r < BOARD_SIZE && 
                    c >= 0 && c < BOARD_SIZE && 
                    gameBoard[r][c] === player
                ) {
                    count++;
                    winningCells.push([r, c]);
                    r += direction * dx;
                    c += direction * dy;
                }
            }
            
            if (count >= WIN_CONDITION) {
                highlightWinningCells(winningCells);
                return true;
            }
        }
        
        return false;
    }
    
    // Highlight winning cells
    function highlightWinningCells(cells) {
        for (const [row, col] of cells) {
            const cell = document.querySelector(`.cell[data-row="${row}"][data-col="${col}"]`);
            cell.classList.add('win-line');
        }
    }
    
    // Check for draw
    function checkDraw() {
        for (let row = 0; row < BOARD_SIZE; row++) {
            for (let col = 0; col < BOARD_SIZE; col++) {
                if (gameBoard[row][col] === '') {
                    return false;
                }
            }
        }
        return true;
    }
    
    // End the game
    function endGame(message) {
        gameActive = false;
        winMessage.textContent = message;
        winMessage.style.display = 'block';
        
        // Apply class based on winner
        winMessage.className = 'win-message';
        if (message.includes('X')) {
            winMessage.classList.add('player-x');
        } else if (message.includes('O')) {
            winMessage.classList.add('player-o');
        }
    }
    
    // Update scores
    function updateScores(winner) {
        if (winner === 'X') {
            scores.X++;
            xScoreDisplay.textContent = scores.X;
        } else if (winner === 'O') {
            scores.O++;
            oScoreDisplay.textContent = scores.O;
        } else {
            scores.draws++;
            drawsDisplay.textContent = scores.draws;
        }
    }
    
    // Restart the game
    function restartGame() {
        gameBoard = Array(BOARD_SIZE).fill().map(() => Array(BOARD_SIZE).fill(''));
        gameActive = true;
        currentPlayer = 'X';
        
        // Update UI
        initializeBoard();
        winMessage.style.display = 'none';
        currentPlayerDisplay.textContent = currentPlayer;
        currentPlayerDisplay.className = 'player-icon player-x';
    }
    
    // Event listeners
    restartButton.addEventListener('click', restartGame);
    
    // Initialize the game
    initializeBoard();
});