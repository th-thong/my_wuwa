import { getGameAccountData } from "@/lib/api"
import { DashboardClient } from "@/components/dashboard-client"

export default async function Home() {
  const { gameAccountData, recentConvenes } = await getGameAccountData()

  return <DashboardClient gameAccountData={gameAccountData} recentConvenes={recentConvenes} />
}
