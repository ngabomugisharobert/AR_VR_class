
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class collision_responder : MonoBehaviour
{
    bool blue;
    bool green;
    bool red;
    bool yellow;
    int counter;

    public Vector3 startForce;
    public Vector3 slowSpeed;
    public Vector3 fastSpeed;
    public Vector3 diameterBig;
    public Vector3 diameterSmall;
    public GameObject beeper;
    public Material color1;
    // Start is called before the first frame update
    void Start()
    {
        Rigidbody rigidbody = GetComponent<Rigidbody>();
        // rigidbody.AddForce(startForce, ForceMode.Impulse);
        blue = true;
    }

    // Update is called once per frame
        void Update()
     {
         if (blue == true)
             gameObject.GetComponent<Renderer> ().material.color = Color.blue;
         if (green == true)
             gameObject.GetComponent<Renderer> ().material.color = Color.green;
         if (yellow == true)
             gameObject.GetComponent<Renderer> ().material.color = Color.yellow;
         if (red == true)
             gameObject.GetComponent<Renderer> ().material.color = Color.red;
     }

void OnCollisionEnter(Collision Collision)
{
    AudioSource aud_dat = beeper.GetComponent(typeof(AudioSource)) as AudioSource;
    aud_dat.Play(0);
                 if (counter == 0)
             {
                 blue = false;
                 green = true;
                 counter = 1;
                 GetComponent<Rigidbody>().transform.localScale = diameterSmall;
                 GetComponent<Rigidbody>().AddForce(slowSpeed, ForceMode.Impulse);
             }
             else if (counter == 1)
             {
                 green = false;
                 yellow = true;
                 counter = 2;
                 GetComponent<Rigidbody>().AddForce(fastSpeed, ForceMode.Impulse);
                 GetComponent<Rigidbody>().transform.localScale = diameterBig;
             }
             else if (counter == 2) 
             {
                 yellow = false;
                 red = true;
                 counter = 3;
                 GetComponent<Rigidbody>().AddForce(slowSpeed, ForceMode.Impulse);
                 GetComponent<Rigidbody>().transform.localScale = diameterSmall;
             }
             else if (counter == 3)
             {
                 red = false;
                 blue = true;
                 counter = 0;
                 GetComponent<Rigidbody>().AddForce(fastSpeed, ForceMode.Impulse);
                 GetComponent<Rigidbody>().transform.localScale = diameterBig;
             }
}


}
