import requests
from typing import Dict, Any
import time

class TeacherClient:
    """Client for interacting with the AI teaching backend service."""
    
    def __init__(self, base_url: str = "http://localhost:5000", timeout: int = 30, max_retries: int = 3):
        """Initialize the TeacherClient.
        
        Args:
            base_url: The URL of the backend service
            timeout: Maximum time (in seconds) to wait for a response
            max_retries: Maximum number of times to retry a failed request
        """
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.max_retries = max_retries
        self.session = requests.Session()

    def send_prompt(self, prompt: str) -> Dict[str, Any]:
        """Send a prompt to the AI and get the response.
        
        Args:
            prompt: The text of the prompt to send
            
        Returns:
            Dict containing the AI's response
            
        Raises:
            ValueError: If prompt is empty or not a string
            requests.exceptions.RequestException: If there's a network error
            TimeoutError: If no response received within timeout
            Exception: For other backend errors
        """
        if not isinstance(prompt, str) or not prompt.strip():
            raise ValueError("Prompt must be a non-empty string")

        # For development/testing, return a mock response
        # Remove this in production and uncomment the actual API calls
        return self._get_mock_response(prompt)

        # Actual API implementation (commented out for now)
        """
        try:
            # Send the initial prompt request
            response = self.session.post(
                f"{self.base_url}/prompt",
                json={"prompt": prompt},
                timeout=self.timeout
            )
            response.raise_for_status()
            data = response.json()
            
            if data.get("status") == "success":
                request_id = data["requestId"]
                return self._wait_for_response(request_id)
            else:
                raise Exception(f"Error sending prompt: {data.get('message', 'Unknown error')}")
                
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network error: {str(e)}")
        """

    def _wait_for_response(self, request_id: str) -> Dict[str, Any]:
        """Poll the backend for a response using the request_id.
        
        Args:
            request_id: The ID of the request to check
            
        Returns:
            Dict containing the AI's response
            
        Raises:
            TimeoutError: If no response received within timeout
            Exception: For backend errors
        """
        start_time = time.time()
        attempts = 0
        
        while attempts < self.max_retries:
            try:
                response = self.session.get(
                    f"{self.base_url}/response/{request_id}",
                    timeout=self.timeout
                )
                response.raise_for_status()
                data = response.json()
                
                if data.get("status") == "pending":
                    if time.time() - start_time > self.timeout:
                        raise TimeoutError("Request timed out waiting for response")
                    time.sleep(1)  # Wait before retrying
                    attempts += 1
                    continue
                    
                return data
                
            except requests.exceptions.RequestException as e:
                attempts += 1
                if attempts >= self.max_retries:
                    raise Exception(f"Failed to get response after {self.max_retries} attempts: {str(e)}")
                time.sleep(1)  # Wait before retrying

        raise Exception("Maximum retry attempts reached")

    def _get_mock_response(self, prompt: str) -> Dict[str, Any]:
        """Generate a mock response for development/testing.
        
        Args:
            prompt: The prompt that was sent
            
        Returns:
            Dict containing a mock response
        """
        # Simple mock responses for testing
        if "what is artificial intelligence" in prompt.lower():
            return {
                "response": """
                Artificial Intelligence (AI) is like a smart computer system that can learn and solve problems. 
                Think of it as a digital brain that can understand language, recognize patterns, and make decisions. 
                Just like how you learn from examples and experience, AI systems learn from large amounts of data 
                to become better at their tasks.
                """
            }
        else:
            return {
                "response": f"This is a mock response to your prompt: '{prompt}'. In production, this would be replaced with actual AI responses."
            }

    def __del__(self):
        """Cleanup method to close the session."""
        self.session.close() 