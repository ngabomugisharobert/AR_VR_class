using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class ResetScene : MonoBehaviour
{


    public Renderer sphere;
    public GameObject Sphere;
    [SerializeField] private Color newColor;
    private Vector3[] vertices;
    private Vector2[] uv;
    // Start is called before the first frame update

    void Start()
    {
        // sphere = Sphere.GetComponent<Renderer>();
        print("the scene started");
        Debug.Log("Test");
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    
public void RestartScene()
{
    SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    Debug.Log("the scene need to restart");
}

public void ChangeMaterial()
{
    Debug.Log("the scene need to restart");
}

}
