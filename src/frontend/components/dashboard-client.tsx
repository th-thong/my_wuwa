"use client"

import { useState } from "react"
import { useRouter } from "next/navigation"
import { Button } from "@/components/ui/button"
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Moon, Sun, Settings } from "lucide-react"
import { useTheme } from "next-themes"
import { SettingsDialog } from "@/components/settings-dialog"
import { Badge } from "@/components/ui/badge"

// Define types for our data
interface GameAccount {
  type: string;
  value: string;
}

interface Convene {
  id: number;
  image: string;
  rarity: number;
  count: number;
  color: string;
}

interface DashboardClientProps {
  gameAccountData: GameAccount[];
  recentConvenes: Convene[];
}

export function DashboardClient({ gameAccountData, recentConvenes }: DashboardClientProps) {
  const router = useRouter()
  const { theme, setTheme } = useTheme()
  const [selectedServer, setSelectedServer] = useState("SEA")
  const [selectedConveneType, setSelectedConveneType] = useState("featured-resonator")
  const [selectedUid, setSelectedUid] = useState("123456789")
  const [settingsOpen, setSettingsOpen] = useState(false)

  return (
    <div className="min-h-screen bg-background">
      <nav className="border-b border-border bg-card">
        <div className="flex h-16 items-center justify-between px-6">
          {/* Left side - Navigation tabs */}
          <div className="flex items-center gap-1">
            <Button variant="default" className="bg-primary text-primary-foreground">
              Home
            </Button>
            <Button variant="ghost" className="text-muted-foreground">
              Resonator
            </Button>
          </div>

          <div className="flex items-center gap-3">
            <Select value={selectedUid} onValueChange={setSelectedUid}>
              <SelectTrigger className="w-[140px]">
                <SelectValue />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="123456789">123456789</SelectItem>
                <SelectItem value="987654321">987654321</SelectItem>
              </SelectContent>
            </Select>
            <Button
              variant="ghost"
              size="icon"
              onClick={() => setTheme(theme === "dark" ? "light" : "dark")}
              className="text-muted-foreground hover:text-foreground"
            >
              {theme === "dark" ? <Sun className="h-5 w-5" /> : <Moon className="h-5 w-5" />}
            </Button>
            <Button variant="outline" className="text-sm bg-transparent">
              Login
            </Button>
            <Button className="text-sm">Register</Button>
            <Button
              variant="ghost"
              size="icon"
              className="text-muted-foreground hover:text-foreground"
              onClick={() => setSettingsOpen(true)}
            >
              <Settings className="h-5 w-5" />
            </Button>
          </div>
        </div>
      </nav>

      <main className="container mx-auto p-6">
        <div className="flex gap-6">
          <div className="w-1/4 rounded-lg border border-border bg-card p-6">
            <h2 className="mb-4 text-xl font-semibold text-foreground">Game Account</h2>

            {/* Server selector and Update button */}
            <div className="mb-4 space-y-3">
              <Select value={selectedServer} onValueChange={setSelectedServer}>
                <SelectTrigger>
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="SEA">SEA</SelectItem>
                  <SelectItem value="AMERICA">AMERICA</SelectItem>
                  <SelectItem value="ASIA">ASIA</SelectItem>
                  <SelectItem value="EUROPE">EUROPE</SelectItem>
                  <SelectItem value="TW">TW</SelectItem>
                  <SelectItem value="HK">HK</SelectItem>
                </SelectContent>
              </Select>
              <Button className="w-full" onClick={() => router.refresh()}>
                Update
              </Button>
            </div>

            {/* Two-column table */}
            <div className="space-y-2">
              {gameAccountData.map((item, index) => (
                <div
                  key={index}
                  className="flex items-center justify-between border-b border-border py-2 last:border-0"
                >
                  <span className="text-sm font-medium text-muted-foreground">{item.type}</span>
                  <span className="text-sm text-foreground">{item.value}</span>
                </div>
              ))}
            </div>
          </div>

          <div className="flex-1 rounded-lg border border-border bg-card p-6">
            <div className="mb-4 flex items-center justify-between">
              <h2 className="text-xl font-semibold text-foreground">Recent Convenes</h2>
              <Select value={selectedConveneType} onValueChange={setSelectedConveneType}>
                <SelectTrigger className="w-[240px]">
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="featured-resonator">Featured Resonator</SelectItem>
                  <SelectItem value="featured-weapon">Featured Weapon</SelectItem>
                  <SelectItem value="permanent-resonator">Permanent Resonator</SelectItem>
                  <SelectItem value="permanent-weapon">Permanent Weapon</SelectItem>
                  <SelectItem value="novice-convene">Novice Convene</SelectItem>
                  <SelectItem value="beginners-choice">Beginner's Choice Convene</SelectItem>
                  <SelectItem value="giveback-event">Giveback Event Convene</SelectItem>
                </SelectContent>
              </Select>
            </div>

            <div className="overflow-x-auto">
              <div className="grid grid-flow-col auto-cols-[80px] gap-3">
                {recentConvenes.map((convene) => (
                  <div key={convene.id} className="relative flex flex-col items-center">
                    <Avatar className="h-20 w-20 ring-2 ring-border">
                      <AvatarImage src={convene.image || "/placeholder.svg"} alt={`Character ${convene.id}`} />
                      <AvatarFallback>C{convene.id}</AvatarFallback>
                    </Avatar>
                    <Badge
                      className={`absolute -bottom-1 h-6 min-w-[28px] justify-center ${
                        convene.color === "emerald"
                          ? "bg-emerald-600 hover:bg-emerald-600"
                          : convene.color === "red"
                            ? "bg-red-600 hover:bg-red-600"
                            : convene.color === "yellow"
                              ? "bg-yellow-600 hover:bg-yellow-600"
                              : convene.color === "blue"
                                ? "bg-blue-600 hover:bg-blue-600"
                                : "bg-violet-600 hover:bg-violet-600"
                      }`}
                    >
                      {convene.count}
                    </Badge>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </main>

      <SettingsDialog open={settingsOpen} onOpenChange={setSettingsOpen} />
    </div>
  )
}
