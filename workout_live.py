func sendWorkoutData(reps: Int, heartRate: Int) {
    guard let url = URL(string: "https://your-api.com/api/workout/live") else { return }
    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    let data: [String: Any] = ["reps": reps, "bpm": heartRate, "user_id": "user123"]
    request.httpBody = try? JSONSerialization.data(withJSONObject: data)
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")
    
    URLSession.shared.dataTask(with: request).resume()
}
