// src/frontend/lib/api.ts

export async function getGameAccountData() {
  // Placeholder data to mimic the API response structure
  const gameAccountData = [
    { type: "Name", value: "Player001" },
    { type: "Uid", value: "123456789" },
    { type: "Waveplates", value: "180/180" },
    { type: "Create Time", value: "2024-05-23" },
    { type: "Average Pity", value: "42.3" },
    { type: "Pull Ratio", value: "1:3.2" },
    { type: "50/50 Wins", value: "3/5" },
  ];

  const recentConvenes = [
    { id: 1, image: "/placeholder-user.jpg", rarity: 5, count: 6, color: "emerald" },
    { id: 2, image: "/placeholder-user.jpg", rarity: 4, count: 72, color: "red" },
    { id: 3, image: "/placeholder-user.jpg", rarity: 5, count: 13, color: "emerald" },
    { id: 4, image: "/placeholder-user.jpg", rarity: 5, count: 3, color: "emerald" },
    { id: 5, image: "/placeholder-user.jpg", rarity: 4, count: 29, color: "emerald" },
    { id: 6, image: "/placeholder-user.jpg", rarity: 5, count: 39, color: "red" },
    { id: 7, image: "/placeholder-user.jpg", rarity: 4, count: 15, color: "emerald" },
    { id: 8, image: "/placeholder-user.jpg", rarity: 4, count: 69, color: "red" }
  ];

  return Promise.resolve({ gameAccountData, recentConvenes });
}
