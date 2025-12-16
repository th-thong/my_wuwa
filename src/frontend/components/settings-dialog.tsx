"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Dialog, DialogContent, DialogHeader, DialogTitle } from "@/components/ui/dialog"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Trash2, Plus } from "lucide-react"

interface GameAccount {
  uid: string
  oauthCode: string
}

interface SettingsDialogProps {
  open: boolean
  onOpenChange: (open: boolean) => void
}

export function SettingsDialog({ open, onOpenChange }: SettingsDialogProps) {
  const [activeTab, setActiveTab] = useState("game-account")
  const [accounts, setAccounts] = useState<GameAccount[]>([
    { uid: "123456789", oauthCode: "abc123xyz" },
    { uid: "987654321", oauthCode: "def456uvw" },
  ])

  const handleAddAccount = () => {
    setAccounts([...accounts, { uid: "", oauthCode: "" }])
  }

  const handleDeleteAccount = (index: number) => {
    setAccounts(accounts.filter((_, i) => i !== index))
  }

  const handleAccountChange = (index: number, field: keyof GameAccount, value: string) => {
    const newAccounts = [...accounts]
    newAccounts[index][field] = value
    setAccounts(newAccounts)
  }

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent className="max-w-3xl">
        <DialogHeader>
          <DialogTitle>Settings</DialogTitle>
        </DialogHeader>

        {/* Horizontal Tabs */}
        <div className="flex gap-1 border-b border-border">
          <Button
            variant={activeTab === "game-account" ? "default" : "ghost"}
            className="rounded-b-none"
            onClick={() => setActiveTab("game-account")}
          >
            Game Account
          </Button>
          <Button
            variant={activeTab === "data" ? "default" : "ghost"}
            className="rounded-b-none"
            onClick={() => setActiveTab("data")}
          >
            Data
          </Button>
        </div>

        {/* Tab Content */}
        <div className="py-4">
          {activeTab === "game-account" && (
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <p className="text-sm text-muted-foreground">Manage your game accounts</p>
                <Button onClick={handleAddAccount} size="sm">
                  <Plus className="mr-2 h-4 w-4" />
                  Add Account
                </Button>
              </div>

              <div className="space-y-3">
                {accounts.map((account, index) => (
                  <div key={index} className="flex items-end gap-3 rounded-lg border border-border bg-card p-4">
                    <div className="flex-1 space-y-2">
                      <Label htmlFor={`uid-${index}`}>UID</Label>
                      <Input
                        id={`uid-${index}`}
                        value={account.uid}
                        onChange={(e) => handleAccountChange(index, "uid", e.target.value)}
                        placeholder="Enter UID"
                      />
                    </div>
                    <div className="flex-1 space-y-2">
                      <Label htmlFor={`oauth-${index}`}>OAuth Code</Label>
                      <Input
                        id={`oauth-${index}`}
                        value={account.oauthCode}
                        onChange={(e) => handleAccountChange(index, "oauthCode", e.target.value)}
                        placeholder="Enter OAuth Code"
                      />
                    </div>
                    <Button variant="destructive" size="icon" onClick={() => handleDeleteAccount(index)}>
                      <Trash2 className="h-4 w-4" />
                    </Button>
                  </div>
                ))}
              </div>
            </div>
          )}

          {activeTab === "data" && (
            <div className="space-y-4">
              <p className="text-sm text-muted-foreground">Data management options</p>
              <div className="rounded-lg border border-border bg-card p-6 text-center">
                <p className="text-muted-foreground">Data settings coming soon...</p>
              </div>
            </div>
          )}
        </div>
      </DialogContent>
    </Dialog>
  )
}
